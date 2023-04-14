from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import auth_user_with_code, get_user_code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/signup/', get_user_code),
    path('api/v1/auth/token/', auth_user_with_code),
    path('api/v1/users/', include('users.urls', namespace='users')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
