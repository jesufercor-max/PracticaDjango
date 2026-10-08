from django.conf import settings
from django.db import models 
from django.utils import timezone

# Create your models here.

# Modelo Anime 
class Anime(models.Model):
    titulo = models.CharField(max_length=150)
    titulo_original= models.CharField(max_length=150)
    sinopsis = models.TextField(max_length=1000)
    anio_estreno = models.IntegerField()
    num_episodios = models.IntegerField()
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='animes/', null=True, blank=True)

# Modelo Plataforma
class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    web = models.URLField()
    logo = models.ImageField(upload_to='plataformas/', null=True, blank=True)
    activa = models.BooleanField(default=True)

# Modelo Disponibilidad
class Disponibilidad(models.Model):
    idioma_audio = models.CharField(max_length=50)
    subtitulos = models.BooleanField(default=False)
    doblaje = models.BooleanField(default=False)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)