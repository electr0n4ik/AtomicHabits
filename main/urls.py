from django.urls import path

from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main import views

app_name = MainConfig.name

# Для получения списка всех привычек: GET /habit/
# Для создания новой привычки: POST /habit/
# Для получения деталей привычки с ID=1: GET /habit/1/
# Для обновления привычки с ID=1: PUT /habit/1/
# Для частичного обновления привычки с ID=1: PATCH /habit/1/
# Для удаления привычки с ID=1: DELETE /habit/1/
router = DefaultRouter()
router.register(r'habit', views.HabitViewSet, basename='habit')

urlpatterns = [
                  path('public_list/', views.HabitViewSet.as_view({"get": "public_list"}), name='public_list'),
              ] + router.urls
