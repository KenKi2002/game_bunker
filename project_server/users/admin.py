from django.contrib import admin

from .models import Game_user

class Game_user_Admin(admin.ModelAdmin):
    list_display = ('login', 'password', 'email', 'image')
    list_display_links = ('login', 'email')
    search_fields = ('login', 'email')

admin.site.register(Game_user, Game_user_Admin)

