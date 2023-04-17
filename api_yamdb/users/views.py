from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
# from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (IsAdminUser, AllowAny, 
                                        IsAuthenticated, IsOwner, 
                                        IsModerator, IsSuperUser)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserSerializer, UserCreateCodeSerializer, UserAuthSerializer
from .permissions import IsOwner, IsSuperUser, IsAdminUser

User = get_user_model()


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser | IsSuperUser,)
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('username',)


class UserDetailSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser | IsSuperUser,)
    serializer_class = UserSerializer
    lookup_field = 'username'
    http_method_names = ['patch', 'get', 'delete']


class UserChangeSet(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(User, username=self.request.user.username)

    def perform_update(self, serializer):
        user = get_object_or_404(User, username=self.request.user.username)
        if serializer.validated_data.get('role') and serializer.validated_data.get('role') != user.role:
            raise PermissionDenied('вы не можете изменять роль своего аккаунта')
        super(UserChangeSet, self).perform_update(serializer)


@api_view(['POST'])
def get_user_code(request):
    if User.objects.filter(username=request.data.get('username')).exists():
        user = User.objects.get(username=request.data.get('username'))
        if user.email != request.data.get('email'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = UserCreateCodeSerializer(data=request.data)
        if serializer.is_valid() and request.data.get('username') != 'me':
            user = User.objects.create_user(
                username=serializer.validated_data.get('username'),
                email=serializer.validated_data.get('email')
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user.confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Код подтверждения.',
        f'Ваш код для регистрации на сайте {user.confirmation_code}.',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )
    return Response(request.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def auth_user_with_code(request):
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = get_object_or_404(User, username=request.user.username)
        confirmation_code = request.query_params.get('confirmation_code')
        if not default_token_generator.check_token(user, confirmation_code):
            return Response('Неправильный код подтверждения', status=status.HTTP_400_BAD_REQUEST)
        token = AccessToken.for_user(user)
        return Response({'token': str(token.access_token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
