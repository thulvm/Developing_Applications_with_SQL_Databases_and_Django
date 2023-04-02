from django.urls import path
from . import views

urlpatterns = [
    path('course_detail', views.course_detail, name='course_detail'),
    path('exam_result', views.exam_result, name='exam_result'),
]
