import json

from django.http import JsonResponse

from .models import Game_rooms, Joined_players



def create_room(request):
    json_data = json.loads(request.body)
    if not Game_rooms.objects.filter(room_name = json_data['name']).exists():
        Game_rooms.objects.create(room_name = json_data['name'], room_password = json_data['password'],
                                  room_settings_player_quantities = json_data['player_quantities'],
                                  room_settings_duration = json_data['duration'],
                                  room_settings_vote_duration = json_data['vote_duration'])
        Joined_players.objects.create(room_name = json_data['name'], player_1 = json_data['creator_login'])
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def join_room(request):
    json_data = json.loads(request.body)
    if Game_rooms.objects.filter(room_name = json_data['name']).exists() and json_data['password'] == Game_rooms.objects.get(room_name = json_data['name']).room_password:
        players_info = Joined_players.objects.get(room_name=json_data['name'])
        if players_info.joined_players_quantities < Game_rooms.objects.get(room_name = json_data['name']).room_settings_player_quantities:
            players_info.joined_players_quantities += 1
            players_info.save()

            exec(f"players_info.player_{players_info.joined_players_quantities} = json_data['incoming_login']")
            players_info.save()
            return JsonResponse({'success': True,
                                 'info': 'all good',
                                 'players': [return_player_name(x+1, json_data['name']) for x in range(players_info.joined_players_quantities)]})
        else:
            return JsonResponse({'success': False, 'info': 'Room is full'})
    else:
        return JsonResponse({'success': False, 'info': 'Incorrect name or password'})

def return_player_name(x, name):
    players = Joined_players.objects.get(room_name=name)
    namespace = {'players': players}
    exec(f'player_name = players.player_{x}', namespace)
    return namespace['player_name']


#'players_image': [exec(f'Game_user.objects.get(login = players_info.player_{x+1}).image') for x in range(players_info.joined_players_quantities)]