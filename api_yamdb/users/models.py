from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models
from django.conf import settings


class User(AbstractUser):
    """Описание модели User, добавление новых полей"""

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(
        validators=[validate_email],
        unique=True,
        blank=False
    )
    bio = models.TextField(blank=True)
    role = models.CharField(
        max_length=10,
        choices=settings.USERS_ROLES,
        default='user'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username
