from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('logup/', users.views.logup, name='logup'),
    # для авторизации
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
