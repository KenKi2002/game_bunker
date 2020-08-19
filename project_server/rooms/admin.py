from django.contrib import admin
from .models import Game_rooms, Joined_players

class Game_rooms_Admin(admin.ModelAdmin):
    list_display = ('room_name', 'room_password', 'room_settings_player_quantities', 'room_settings_duration', 'room_settings_vote_duration', 'room_joined_players')
    list_display_links = ('room_name', 'room_settings_player_quantities')
    search_fields = ('room_name', 'room_settings_player_quantities')

class Game_joined_players_Admin(admin.ModelAdmin):
    list_display = ('room_name', 'joined_players_quantities')
    list_display_links = ('room_name', 'joined_players_quantities')
    search_fields = ('room_name', 'joined_players_quantities')

admin.site.register(Game_rooms, Game_rooms_Admin)
admin.site.register(Joined_players, Game_joined_players_Admin)