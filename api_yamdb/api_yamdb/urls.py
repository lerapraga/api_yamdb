from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/auth/', include('auth.urls', namespace='auth')),
    path('api/v1/users/', include('users.urls', namespace='users')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
