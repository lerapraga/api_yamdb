from django.urls import path
from .views import UserViewSet, UserDetailSet, UserChangeSet

app_name = 'users'

urlpatterns = [
    path('', UserViewSet.as_view(), name='user_view'),
    path('<slug:username>/', UserDetailSet.as_view(), name='user_detail'),
    path('me/', UserChangeSet.as_view(), name='user_change'),
]
