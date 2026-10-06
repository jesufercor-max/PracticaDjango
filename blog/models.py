from django.conf import settings
from django.db import models 
from django.utils import timezone

# Create your models here.

# Modelo Animal

class Animal(models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    CATEGORIAS = [
        ("ANFI", "Anfibios"),
        ("FEL","Felinos"),
        ("REP","reptiles"),
    ]   
    
    tipo = models.CharField(
        max_length=4,
        choices=CATEGORIAS,
        default="FEL",
    )
    
class Protectora(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    fecha_creacion = models.DateField()
    
class Colaborador(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    fecha_entrada_protectora = models.DateTimeField(null=True)
