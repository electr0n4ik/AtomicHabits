from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password])

    def create(self, validated_data):
        email = validated_data['email']
        user = get_user_model().objects.create_user(
            email=email,
            password=validated_data['password'],
            tg_id=validated_data['tg_id'],
            username=email[0:email.index('@')]
        )
        return user

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'phone', 'city', 'avatar', 'tg_id']
