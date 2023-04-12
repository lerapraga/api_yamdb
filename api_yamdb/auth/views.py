# from django.contrib.auth import get_user_model
# from django.core.mail import send_mail
# from rest_framework import status
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
#
# from .models import ConfirmCode
#
# User = get_user_model()
#
#
# def signup(request):
#     if request.user.username != 'me':
#         confirm_code = ConfirmCode.objects.create(user=request.user)
#         send_mail(
#             'Код подтверждения.',
#             f'Ваш код для регистрации на сайте {confirm_code.code}.',
#             'from@example.com',
#             [request.user.email],
#             fail_silently=False,
#         )
#     return Response(status=status.HTTP_200_OK)
#
#
# # def check_confirm_code(request, code):
# #      user = get_object_or_404(ConfirmCode, code=code)
