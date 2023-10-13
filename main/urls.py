# from django.urls import path
#
# from knowledge.apps import KnowledgeConfig
# from rest_framework.routers import DefaultRouter
#
# from knowledge import views
#
# app_name = KnowledgeConfig.name
#
# # Для получения списка всех курсов: GET /course/
# # Для создания нового курса: POST /course/
# # Для получения деталей курса с ID=1: GET /course/1/
# # Для обновления курса с ID=1: PUT /course/1/
# # Для частичного обновления курса с ID=1: PATCH /course/1/
# # Для удаления курса с ID=1: DELETE /course/1/
# router = DefaultRouter()
# router.register(r'course', views.CourseViewSet, basename='course')
#
# urlpatterns = [
#                   path('lesson/create/', views.LessonCreateAPIView.as_view(), name='lesson-create'),
#                   path('lesson/', views.LessonListAPIView.as_view(), name='lesson-list'),
#                   path('lesson/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson-once'),
#                   path('lesson/update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson-upd'),
#                   path('lesson/delete/<int:pk>/', views.LessonDestroyAPIView.as_view(), name='lesson-del'),
#
#                   path('payment/', views.PaymentRetrieveAPIView.as_view(), name='retrieve_payment'),
#                   path('payment/create/', views.PaymentCreateAPIView.as_view(), name='create_payment'),
#                   path('course/<int:pk>/sub/',
#                        views.CourseViewSet.as_view({'post': 'sub'}),
#                        name='course-sub'),
#                   path('course/<int:pk>/unsub/',
#                        views.CourseViewSet.as_view({'post': 'unsub'}),
#                        name='course-unsub')
#
#               ] + router.urls