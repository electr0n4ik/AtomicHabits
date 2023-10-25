from django.core.management import BaseCommand
from django.utils import timezone

from users.models import User
from main.models import Habit


class Command(BaseCommand):

    def handle(self, *args, **options):
        superuser, _ = User.objects.get_or_create(
            email='superuser@gmail.com',
            username='superuser',
            defaults={'is_superuser': True, 'is_staff': True}
        )
        superuser.set_password('superuser')
        superuser.save()

        user1, _ = User.objects.get_or_create(
            email='user1@gmail.com',
            username='user1',
            tg_id='id_psi'
        )
        user1.set_password('user1')
        user1.save()

        habit_list = [
            {"owner": superuser, "location": "Moscow",
             "action": "Python", "action_time": timezone.now(),
             "timing": "daily", "is_publish": True},
            {"owner": user1, "location": "Moscow",
             "action": "Python",
             "action_time": timezone.now(), "timing": "daily"}

        ]
        for element in habit_list:
            Habit.objects.create(**element)
