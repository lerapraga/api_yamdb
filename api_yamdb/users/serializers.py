from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.conf import settings

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели user"""

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        lookup_field = 'username'

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Такой email уже зарегистрирован у другого пользователя')
        return value


class UserCreateCodeSerializer(serializers.ModelSerializer):
    """Сериализатор для POST запроса при создании пользователя на получение confirm_code"""

    username = serializers.CharField(
        validators=[
            UniqueValidator(User.objects.all()),
            RegexValidator(r'^[\w.@+-]+$'),
        ],
        max_length=150
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(User.objects.all())],
        max_length=254
    )

    class Meta:
        model = User
        fields = ('username', 'email')


class UserAuthSerializer(serializers.ModelSerializer):
    """Сериализатор для POST запроса на получение токена"""

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
