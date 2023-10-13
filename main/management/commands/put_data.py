from django.core.management import BaseCommand
from django.utils import timezone

from users.models import User
from main.models import Habit


class Command(BaseCommand):

    def handle(self, *args, **options):
        superuser, _ = User.objects.get_or_create(
            email='superuser@gmail.com',
            defaults={'is_superuser': True, 'is_staff': True}
        )
        superuser.set_password('superuser')
        superuser.save()

        manager, _ = User.objects.get_or_create(
            email='manager@gmail.com',
            defaults={'is_staff': True}
        )
        manager.set_password('manager')
        manager.save()

        user1, _ = User.objects.get_or_create(
            email='user1@gmail.com'
        )
        user1.set_password('user1')
        user1.save()

        user2, _ = User.objects.get_or_create(
            email='user2@gmail.com'
        )
        user2.set_password('user2')
        user2.save()

        user3, _ = User.objects.get_or_create(
            email='andreyshka3@gmail.com'
        )
        user3.set_password('user3')
        user3.save()

        habit_list = [
            {"owner": superuser, "location": "Moscow", "action": "Python", "action_time": timezone.now(),
             "timing": "daily"},
            {"owner": manager, "location": "Moscow", "action": "Python", "action_time": timezone.now(),
             "timing": "daily"},
            {"owner": user1, "location": "Moscow", "action": "Python", "action_time": timezone.now(), "timing": "daily"}

        ]
        for element in habit_list:
            Habit.objects.create(**element)
