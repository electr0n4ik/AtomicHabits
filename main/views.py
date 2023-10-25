import json
import requests
from django.conf import settings
from django.http import HttpResponse
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Habit
from .pagination import MyPagination
from .permissions import IsOwner
from .serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с моделью."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.order_by('id')
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination
    token_bot = settings.TELEGRAM_BOT_TOKEN
    url_get_chat_id = \
        f'https://api.telegram.org/bot{token_bot}/getUpdates'
    url_send_msg = \
        f'https://api.telegram.org/bot{token_bot}/sendMessage'

    def list(self, request, *args, **kwargs):

        self.permission_classes = [IsOwner]
        user = request.user
        habits = self.queryset.filter(owner=user)
        page = self.paginate_queryset(habits)
        serializer = HabitSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):

        owner = request.user
        habit_data = request.data
        serializer = HabitSerializer(
            data=habit_data,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()
            user_id = owner.tg_id
            message = (f'{serializer.data["action"]} in '
                       f'{serializer.data["location"]}')

            # Создаем интервал для повтора задачи
            if serializer.data['timing'] == 'weekly':
                interval_data = {
                    'weekly': 24 * 7 * 3600,  # Интервал в секундах
                    'period': IntervalSchedule.SECONDS,
                }
            else:
                interval_data = {
                    'every': 24 * 3600,  # Интервал в секундах
                    'period': IntervalSchedule.SECONDS,
                }

            schedule, _ = IntervalSchedule.objects.get_or_create(
                **interval_data)

            arg1 = user_id
            arg2 = f'{habit_data["action"]} in {habit_data["location"]}'

            response_get_chat_id = requests.get(self.url_get_chat_id)

            data_get_chat_id = response_get_chat_id.json()

            if data_get_chat_id['ok']:
                for i in data_get_chat_id['result']:
                    if i['message']['from']['username'] == user_id:
                        chat_id = i['message']['chat']['id']
                        requests.post(self.url_send_msg, params={
                            'chat_id': chat_id,
                            'text': f"You should do: {message}! JUST DO IT!"
                        })

                        # Создаем задачу для повторения
                        task = PeriodicTask.objects.create(
                            interval=schedule,
                            name=f'{user_id}_{habit_data["action"]}',
                            task=f'main.tasks.send_tg_not_{user_id}',
                            args=json.dumps([arg1, arg2])
                        )

                        task.save()

                        return Response(serializer.data,
                                        status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def public_list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        queryset = queryset.filter(is_publish=True)
        page = self.paginate_queryset(queryset)

        serializer = HabitSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)


def update(self, request, *args, **kwargs):
    self.permission_classes = [IsOwner]
    owner = request.user
    habit_data = request.data
    serializer = HabitSerializer(
        data=habit_data,
        context={'request': request}
    )

    if serializer.is_valid():
        serializer.save()
        user_id = owner.tg_id
        message = (f'{serializer.data["action"]} in '
                   f'{serializer.data["location"]}')

        # Создаем интервал для повтора задачи
        interval_data = {
            'every': 10,  # Интервал в секундах
            'period': IntervalSchedule.SECONDS,
        }

        schedule, _ = IntervalSchedule.objects.get_or_create(
            **interval_data)

        arg1 = user_id
        arg2 = f'{habit_data["action"]} in {habit_data["location"]}'

        response_get_chat_id = requests.get(self.url_get_chat_id)

        data_get_chat_id = response_get_chat_id.json()

        if data_get_chat_id['ok']:
            for i in data_get_chat_id['result']:
                if i['message']['from']['username'] == user_id:
                    chat_id = i['message']['chat']['id']
                    requests.post(self.url_send_msg, params={
                        'chat_id': chat_id,
                        'text': f"You should do: {message}! JUST DO IT!"
                    })

                    # Создаем задачу для повторения
                    task = PeriodicTask.objects.create(
                        interval=schedule,
                        name=f'{user_id}_habit_task1',
                        task=f'main.tasks.send_tg_not_{user_id}',
                        args=json.dumps([arg1, arg2])
                    )

                    task.save()

                    # Вызываем функцию send_tg_not для отправки уведомления
                    # send_tg_not(user_id, message)
                    return HttpResponse("Курс успешно обновлен")

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
