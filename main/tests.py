# from rest_framework import response, status
# from rest_framework.test import APITestCase
# from rest_framework_simplejwt.tokens import RefreshToken
#
# from .models import Habit
# from users.models import User
#
#
# class HabitTestCase(APITestCase):
#     """coverage run --source='.' manage.py test"""
#     """coverage report"""
#
#     def setUp(self):
#         """Тестовые данные."""
#         self.user = User.objects.create(email='testuser@example.com', password='testpassword')
#
#         refresh = RefreshToken.for_user(self.user)
#         self.access_token = str(refresh.access_token)
#
#         self.course = Course.objects.create(
#             title="Test Course setUp",
#             description="This is a test course.",
#             owner=self.user
#         )
#
#         self.lesson1 = Lesson.objects.create(
#             course=self.course,
#             title="Test Lesson setUp",
#             description="This is a test lesson setUp.",
#             url_video="https://youtube.com/video",
#             owner=self.user
#         )
#
#         self.lesson2 = Lesson.objects.create(
#             course=self.course,
#             title="Test Lesson setUp",
#             description="This is a test lesson setUp.",
#             url_video="https://youtube.com/video",
#             owner=self.user
#         )
#
#         self.lesson3 = Lesson.objects.create(
#             course=self.course,
#             title="Test Lesson setUp",
#             description="This is a test lesson setUp.",
#             url_video="https://youtube.com/video",
#             owner=self.user
#         )
#
#     def test_create_lesson(self):
#         """Тест создания урока."""
#         data = {
#             'course': self.course.pk,
#             'title': 'Test Lesson create',
#             'description': 'Test Lesson Description',
#             'url_video': 'https://youtube.com/video',
#         }
#
#         response = self.client.post('/lesson/create/', data=data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#     def test_list_lesson(self):
#         """Тест просмотра уроков."""
#
#         response = self.client.get(
#             '/lesson/',
#             HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
#         )
#         print(response.json())
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#     def test_update_lesson(self):
#         """Тест обновления урока."""
#         data = {
#             'title': 'Test Update Lesson'
#         }
#
#         response = self.client.patch(
#             f'/lesson/update/{self.lesson2.id}',
#             data=data,
#             HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#     def test_delete_lesson(self):
#         """Тест удаления урока."""
#
#         response = self.client.delete(
#             f'/lesson/delete/{self.lesson3.id}',
#             HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_204_NO_CONTENT
#         )
#