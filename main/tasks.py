# import os
#
# from celery import shared_task
# from django.core.mail import send_mail
# from django.utils import timezone
# from dotenv import load_dotenv
# from pathlib import Path
#
# from users.models import User
#
# BASE_DIR = Path(__file__).resolve().parent.parent
# env_path = BASE_DIR / '.env'
# load_dotenv(dotenv_path=env_path)
# # celery -A config worker --loglevel=info
#
#
# @shared_task
# def send_update_notification(email, course_name):
#     subject = 'Уведомление об обновлении курса'
#     message = f'Курс "{course_name}" был обновлен. Проверьте новый материал!'
#     from_email = os.getenv('EMAIL_HOST_USER')
#     recipient_list = [email]
#
#     send_mail(subject, message, from_email, recipient_list)
#
#
# @shared_task
# def block_inactive_users():
#     one_month_ago = timezone.now() - timezone.timedelta(days=30)
#
#     # Находим пользователей, которые не заходили более месяца
#     users_to_block = User.objects.filter(last_login__lte=one_month_ago, is_active=True)
#
#     # Блокируем пользователей
#     for user in users_to_block:
#         user.is_active = False
#         user.save()
#