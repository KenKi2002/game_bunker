from django.contrib import admin
from django.urls import path, include
from users.views import connect_with_server, load_prof_image
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('user/', include('users.urls')),
    path('room/', include('rooms.urls')),
    path('admin/', admin.site.urls),
    path('connect/', connect_with_server),
    path('load_image/', load_prof_image)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
