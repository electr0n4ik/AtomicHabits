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
    # queryset = Habit.objects.all()
    queryset = Habit.objects.order_by('id')
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]

    def create(self, request, *args, **kwargs):
        owner = request.user
        habit_data = request.data
        habit_data['owner'] = owner.id
        serializer = HabitSerializer(data=habit_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def public_list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = HabitSerializer(queryset, many=True, context={'request': request})
        # if request:
        #     return Response(serializer.data)
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
