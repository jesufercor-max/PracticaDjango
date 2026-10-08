# 🐾 Sistema de Gestión de Protectoras y Animales (Django)

Proyecto web en **Django** orientado a la administración y registro de animales resguardados, protectoras asociadas y personal colaborador.

---

## 📌 Tabla de Contenidos

1. [1. Modelos de Datos (`models.py`)](#1-modelos-de-datos-modelspy)
2. [2. Configuración de Rutas (`urls.py`)](#2-configuración-de-rutas-urlspy)
3. [3. Controladores y Vistas (`views.py`)](#3-controladores-y-vistas-viewspy)
4. [4. Plantillas HTML y Estilos CSS (`templates/`)](#4-plantillas-html-y-estilos-css-templates)

---

## 1. Modelos de Datos (`models.py`)

Definición de las clases de la base de datos para registrar usuarios cuidadores, especies de animales, organizaciones protectoras y sus colaboradores:

```python
from django.conf import settings
from django.db import models 
from django.utils import timezone

# Modelo Animal
class Animal(models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    CATEGORIAS = [
        ("ANFI", "Anfibios"),
        ("FEL", "Felinos"),
        ("REP", "Reptiles"),
    ]   
    
    tipo = models.CharField(
        max_length=4,
        choices=CATEGORIAS,
        default="FEL",
    )

# Modelo Protectora
class Protectora(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    fecha_creacion = models.DateField()

# Modelo Colaborador
class Colaborador(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    fecha_entrada_protectora = models.DateTimeField(null=True)
```

---

## 2. Configuración de Rutas (`urls.py`)

Rutas principales asignadas a la navegación de animales, protectoras y colaboradores:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animales/', views.mostrar_animales, name='post_animales'),
    path('protectoras/', views.mostrar_protetcoras, name='post_protectoras'),
    path('colaboradores/', views.mostrar_colaboradores, name='post_colaboradores'),
]
```

---

## 3. Controladores y Vistas (`views.py`)

Funciones encagadas de obtener los registros de la base de datos y pasarlos al contexto de las plantillas HTML:

```python
from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

def index(request):
    return render(request, 'index.html')

def mostrar_animales(request):
    posts = Animal.objects.all()
    return render(request, 'post_animales.html', {'mostrar_post_anaimales': posts})

def mostrar_protetcoras(request):
    post = Protectora.objects.all()
    return render(request, 'post_protectoras.html', {'mostrar_post_protectoras': post}) 

def mostrar_colaboradores(request):
    post = Colaborador.objects.all()
    return render(request, 'post_colaboradores.html', {'mostrar_post_colaboradores': post}) 
```

---

## 4. Plantillas HTML y Estilos CSS (`templates/`)

### Vista Colaboradores (`post_colaboradores.html`)

Muestra el listado de colaboradores con sus nombres y cargos desempeñados dentro de la protectora, usando estilos adaptados en verde esmeralda.

```html
<main class="contenedor">
    <!-- Tabla Estilizada -->
    <table class="tabla-colaboradores">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Cargo</th>
            </tr>
        </thead>
        <tbody>
            {% for colaboradores in mostrar_post_colaboradores %}
            <tr>
                <td>{{ colaboradores.nombre }}</td>
                <td><strong>{{ colaboradores.cargo }}</strong></td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</main>

<div class="regreso">
    <a href="{% url 'index' %}">Volver</a>
</div>

<!-- Estilos CSS -->
<style>
    .contenedor {
        max-width: 1000px;
        margin: 20px auto;
        padding: 0 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .tabla-colaboradores {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        border-radius: 8px 8px 0 0;
        overflow: hidden;
    }
    .tabla-colaboradores thead tr {
        background-color: #009879;
        color: #ffffff;
        text-align: left;
        font-weight: bold;
    }
    .tabla-colaboradores th, .tabla-colaboradores td {
        padding: 12px 15px;
    }
    .tabla-colaboradores tbody tr {
        border-bottom: 1px solid #dddddd;
    }
    .tabla-colaboradores tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
    .tabla-colaboradores tbody tr:last-of-type {
        border-bottom: 2px solid #009879;
    }
    .regreso a {
        color: #008000;
    }
</style>
```