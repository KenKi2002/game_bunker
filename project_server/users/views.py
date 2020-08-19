from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Game_user
import json


def login(request):
    json_data = json.loads(request.body)
    login = json_data['login']
    password = json_data['password']
    # login_array = [[i for i in f.values()][0] for f in Game_user.objects.values('login')]
    if Game_user.objects.filter(login=login).exists():
        db_user = Game_user.objects.get(login=login)
        if password == db_user.password:
            return JsonResponse({'success': True,})
        else:
            return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': False})

def signup(request):
    json_data = json.loads(request.body)
    login = json_data['login']
    password = json_data['password']
    #login_array = [[i for i in f.values()][0] for f in Game_user.objects.values('login')]
    if not Game_user.objects.filter(login=login).exists():
        Game_user.objects.create(login=login,password=password)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@csrf_exempt
def load_prof_image(request):
    User = Game_user.objects.get(login= request.POST['login'])
    if not Game_user.objects.filter(image_name = request.POST['image_name']).exists():
        if request.method == 'POST':
            User.image = request.FILES['image']
            User.image_name = request.POST['image_name']
            User.save()
            return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'info': f"file with name {request.POST['image_name']} already loaded on server"})


def connect_with_server(request):
    return JsonResponse({'success': True})

def return_image_path(request):
    json_data = json.loads(request.body)
    User = Game_user.objects.get(login=json_data['login'])
    if User.image_name != 'None':
        return JsonResponse({'success': True, 'path': User.image_name})
    else:
        return JsonResponse({'success': False, 'info': 'image didn`t loaded'})

