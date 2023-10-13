from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Habit
from .paginators import MyPagination
from .permissions import IsOwnerOrStaff
from .serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с моделью."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = HabitSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     course_id = kwargs.get('pk')
    #     course = Habit.objects.get(pk=course_id)
    #
    #     course.last_updated = timezone.now()
    #     course.save()
    #
    #     users = CourseSubscription.objects.filter(subscribed=True, course=course)
    #
    #     for subscription in users:
    #         user = subscription.user
    #         email = user.email
    #         send_update_notification.delay(email, course.title)
    #
    #     return HttpResponse("Курс успешно обновлен")
