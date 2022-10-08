from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('1 course/', views.first_course),
    path('2 course/', views.second_course),
    path('3 course/', views.third_course),
    path('4 course/', views.fourth_course)
    
]
