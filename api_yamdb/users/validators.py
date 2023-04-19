from rest_framework.serializers import ValidationError


def not_me_username(username):
    if username.lower() == 'me':
        raise ValidationError('Нельзя использовать "me" в качестве username')
