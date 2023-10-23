from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """coverage run --source='.' manage.py test"""
    """coverage report"""

    def setUp(self):
        """Тестовые данные."""
        self.user = User.objects.create(email='testuser@example.com',
                                        password='testpassword',
                                        tg_id='id_psi')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.habit = Habit.objects.create(
            location="Moscow",
            action_time="2023-10-13T13:56:09.386363Z",
            action="run to shop",
            is_nice=False,
            timing="daily",
            is_publish=True,
            reward="test gift",
            execution_time=5,
            last_completed="2023-10-13",
            owner_id=self.user.id
        )

    def test_create_habit(self):
        data = {
            "location": "Moscow",
            "action_time": "2023-10-13T13:56:09.386363Z",
            "action": "run to shop",
            "is_nice": False,
            "timing": "daily",
            "is_publish": True,
            "reward": "test gift",
            "execution_time": 5,
            "last_completed": "2023-10-13"
        }

        response = self.client.post(
            '/habit/', data=data,
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habit(self):
        response = self.client.get(
            '/habit/public_list/',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        data = {
            'location': 'SkyProCity',
            "action_time": "2023-10-13T13:56:09.386363Z",
            "action": "run to shop",
            "is_nice": False,
            "timing": "daily",
            "is_publish": True,
            "reward": "test gift",
            "execution_time": 5,
            "last_completed": "2023-10-13"
        }

        response = self.client.put(
            f'/habit/{self.habit.id}/',
            data=data,
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        response = self.client.delete(
            f'/habit/{self.habit.id}/',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
