from django.urls import path
from .views import create_room, join_room

urlpatterns = [
    path('create/',create_room, name='create'),
    path('join/',join_room, name='join'),
]