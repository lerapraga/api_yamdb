from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, validate_email
from django.db import models


class User(AbstractUser):
    """Описание модели User, добавление новых полей"""

    username = models.CharField(
        max_length=150,
        validators=[RegexValidator(r'^[\w.@+-]+$')],
        unique=True
    )
    email = models.EmailField(
        max_length=254,
        validators=[validate_email],
    )
    bio = models.TextField(blank=True)
    role = models.CharField(
        max_length=10,
        choices=settings.USERS_ROLES,
        default='user'
    )
    confirmation_code = models.CharField(max_length=100, blank=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
