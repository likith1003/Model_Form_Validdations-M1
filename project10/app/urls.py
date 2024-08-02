from django.urls import path
from .views import *
urlpatterns = [
    path('insert_skool', insert_skool, name='insert_skool'),
    path('register', register, name='register'),
    path('student', student, name='student')

]
