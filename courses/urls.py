from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/enroll/', views.enroll_course, name='enroll_course'),
    path('courses/<int:course_pk>/lessons/<int:lesson_pk>/', views.lesson_detail, name='lesson_detail'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('quiz/<int:quiz_pk>/', views.quiz_view, name='quiz_view'),
]
