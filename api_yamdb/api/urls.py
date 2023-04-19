from django.urls import include, path
from rest_framework.routers import SimpleRouter

from users.views import auth_user_with_code, get_user_code

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

app_name = 'api'

router_v1 = SimpleRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('categories', CategoryViewSet, basename='сategories')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/auth/signup/', get_user_code),
    path('v1/auth/token/', auth_user_with_code),
    path('v1/', include(router_v1.urls)),
]
