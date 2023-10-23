from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .apps import UsersConfig
from .views import UserRegistrationView

app_name = UsersConfig.name

urlpatterns = [
    path('logup/', UserRegistrationView.as_view(), name='logup'),
    # для авторизации
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]
