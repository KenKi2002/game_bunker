from django.db import models

class Game_rooms(models.Model):
    room_name = models.CharField(max_length=50, verbose_name='name')
    room_password = models.CharField(max_length=50, verbose_name='password')
    room_settings_player_quantities = models.IntegerField(verbose_name='player_quantities')
    room_settings_duration = models.IntegerField(verbose_name='duration')
    room_settings_vote_duration = models.IntegerField(verbose_name='vote_duration')
    room_joined_players = models.ForeignKey('joined_players', null=True, on_delete=models.CASCADE)

class Joined_players(models.Model):
    room_name = models.CharField(max_length=50)
    joined_players_quantities = models.IntegerField(default=0, null=True)
    player_1 = models.CharField(max_length=100, null=True)
    player_2 = models.CharField(max_length=100, null=True)
    player_3 = models.CharField(max_length=100, null=True)
    player_4 = models.CharField(max_length=100, null=True)
    player_5 = models.CharField(max_length=100, null=True)
    player_6 = models.CharField(max_length=100, null=True)
    player_7 = models.CharField(max_length=100, null=True)
    player_8 = models.CharField(max_length=100, null=True)
    player_9 = models.CharField(max_length=100, null=True)
    player_10 = models.CharField(max_length=100, null=True)
    player_11 = models.CharField(max_length=100, null=True)
    player_12 = models.CharField(max_length=100, null=True)




