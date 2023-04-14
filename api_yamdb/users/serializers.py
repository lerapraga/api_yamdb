from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели user"""

    username = serializers.CharField(
        validators=[RegexValidator(r'^[\w.@+-]+$')],
        max_length=150
    )
    email = serializers.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')


class UserLoginCodeSerializer(serializers.ModelSerializer):
    """Сериализатор для POST запроса при логине пользователя на получение confirm_code"""

    class Meta:
        model = User
        fields = ('username', 'email')


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

    username = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        validators=[UniqueValidator(User.objects.all())],
        slug_field='username'
    )
    confirmation_code = serializers.CharField(read_only=True)
    token = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code', 'token')
