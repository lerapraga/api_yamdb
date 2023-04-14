# from random import randint
#
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.db import models
#
# User = get_user_model()
#
#
# def create_confirm_code():
#     code = []
#     for _ in range(settings.NUMBER_CONFIRM_CODE):
#         code.append(str(randint(0, 9)))
#     return ''.join(code)
#
#
# class ConfirmCode(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     code = models.CharField(
#         max_length=settings.NUMBER_CONFIRM_CODE,
#         default=create_confirm_code()
#     )
