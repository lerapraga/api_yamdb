from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email, RegexValidator
from django.db import models
from django.conf import settings


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
    is_moderator = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username
