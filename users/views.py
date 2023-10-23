from rest_framework import generics
from .models import User
from rest_framework import status
from rest_framework.response import Response

from users.serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'status': 'User registered successfully'},
            status=status.HTTP_201_CREATED, headers=headers)
