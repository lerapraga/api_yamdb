from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.serializers import ReviewsSerializer
from api.permissions import AdminAuthorModeratorOrReadOnly
from reviews.models import Title

# from django.core.mail import EmailMessage
from api.filters import TitleFilter
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators import action
# from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .mixins import ModelMixinSet
from .permissions import IsAdminUserOrReadOnly
from .serializers import (TitleReadSerializer, TitleWriteSerializer)

# from rest_framework_simplejwt.tokens import RefreshToken


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = (AdminAuthorModeratorOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class UsersViewSet(viewsets.ModelViewSet):
    pass


class APIGetToken(APIView):
    """
    Получение JWT-токена в обмен на username и confirmation code.
    Права доступа: Доступно без токена. Пример тела запроса:
    {
        "username": "string",
        "confirmation_code": "string"
    }
    """
    pass


class APISignup(APIView):
    """
    Получить код подтверждения на переданный email. Права доступа: Доступно без
    токена. Использовать имя 'me' в качестве username запрещено. Поля email и
    username должны быть уникальными. Пример тела запроса:
    {
        "email": "string",
        "username": "string"
    }
    """
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CategoryViewSet(ModelMixinSet):
    """
    Получить список всех категорий. Права доступа: Доступно без токена
    """
    pass


class GenreViewSet(ModelMixinSet):
    """
    Получить список всех жанров. Права доступа: Доступно без токена
    """
    pass


class TitleViewSet(ModelViewSet):
    """
    Получить список всех объектов. Права доступа: Доступно без токена
    """
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).all()
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer
