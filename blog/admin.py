from django.contrib import admin
from .models import Anime, Plataforma, Disponibilidad

# Register your models here.

admin.site.register(Anime)
admin.site.register(Plataforma)
admin.site.register(Disponibilidad)