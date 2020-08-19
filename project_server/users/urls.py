from django.urls import path
from .views import login, signup, return_image_path

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('login/',login, name='login'),
    path('return_path/', return_image_path)
]