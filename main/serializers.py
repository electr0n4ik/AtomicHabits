from rest_framework import serializers
from .models import Habit


# class HabitSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     owner = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )
#     location = serializers.CharField(max_length=127)
#     action_time = serializers.DateTimeField()
#     action = serializers.CharField()
#     is_nice = serializers.BooleanField()
#     timing = serializers.CharField()
#     reward = serializers.CharField()
#     execution_time = serializers.IntegerField()
#     is_publish = serializers.BooleanField()
#     last_completed = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Habit.objects.create(**validated_data)
#
#     class Meta:
#         model = Habit
#         fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def create(self, validated_data):
        return Habit.objects.create(**validated_data)

    class Meta:
        model = Habit
        fields = '__all__'
