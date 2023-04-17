from django.urls import path

from .views import UserViewSet, UserDetailSet, UserChangeSet

app_name = 'users'

urlpatterns = [
    path('', UserViewSet.as_view()),
    path('me/', UserChangeSet.as_view()),
    path('<str:username>/', UserDetailSet.as_view()),
]
