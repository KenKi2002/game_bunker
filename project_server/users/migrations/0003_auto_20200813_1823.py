# Generated by Django 3.1 on 2020-08-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200810_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_user',
            name='image',
            field=models.ImageField(default='Game_bunker.templates.users.def_prof_img.png', null=True, upload_to='', verbose_name='image'),
        ),
    ]
