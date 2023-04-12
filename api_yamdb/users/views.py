from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import UserSerializer
from .permissions import IsOwner
from rest_framework import generics


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('username',)


class UserDetailSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))


class UserChangeSet(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated & IsOwner,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))
