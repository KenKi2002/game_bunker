from django.db import models

class Game_user(models.Model):
    login = models.CharField(max_length=50, verbose_name='login')
    password = models.CharField(max_length=50, verbose_name='password')
    email = models.EmailField(verbose_name='email')
    image_name = models.CharField(max_length=200, default='None', null=True)
    image = models.FileField(upload_to='templates/users', null=True)

