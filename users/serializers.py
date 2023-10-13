from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = "__all__"
