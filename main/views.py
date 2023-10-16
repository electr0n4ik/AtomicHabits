from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .tasks import send_telegram_notification
from .models import Habit
from .paginators import MyPagination
from .permissions import IsOwnerOrStaff
from .serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с моделью."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.order_by('id')
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]

    def list(self, request):
        user = request.user
        habits = self.queryset.filter(owner=user)
        serializer = self.get_serializer(habits, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        owner = request.user

        habit_data = request.data
        serializer = HabitSerializer(data=habit_data, context={'request': request})

        if serializer.is_valid():
            serializer.save()

            user_id = owner.tg_id

            send_telegram_notification(user_id, f'{serializer.data["action"]} in {serializer.data["location"]}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def public_list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if 'is_publish' in request.query_params:
            is_publish = request.query_params.get('is_publish')
            queryset = queryset.filter(is_publish=is_publish)
        else:
            queryset = queryset.filter(owner=request.user)

        serializer = HabitSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        owner = request.user

        habit_data = request.data
        serializer = HabitSerializer(data=habit_data, context={'request': request})

        if serializer.is_valid():
            serializer.save()

            user_id = owner.tg_id

            send_telegram_notification(user_id, f'Action updated: {serializer.data["action"]} in {serializer.data["location"]}')

        return HttpResponse("Курс успешно обновлен")
