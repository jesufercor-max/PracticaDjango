stema de Gestión de Protectoras y Animales (Django)

Proyecto web en **Django** orientado a la administración y registro de animales resguardados, protectoras asociadas y personal colaborador.
nimes y Plataformas (Django)

Proyecto web desarrollado en **Django** para la consulta, gestión y despliegue de información sobre animes, plataformas de streaming y su disponibilidad de catálogo.



1. [1. Modelos de Datos (`models.py`)](#1-modelos-de-datos-modelspy)
2. [2. Configuración de Rutas (`urls.py`)](#2-configuración-de-rutas-urlspy)
3. [3. Controladores y Vistas (`views.py`)](#3-controladores-y-vistas-viewspy)
4. [4. Plantillas HTML y Estilos CSS (`templates/`)]
- [1. Modelos de Datos (`models.py`)](#1-modelos-de-datos-modelspy)
- [2. Configuración de Rutas (`urls.py`)](#2-configuración-de-rutas-urlspy)
- [3. Controladores y Vistas (`views.py`)](#3-controladores-y-vistas-viewspy)
- [4. Plantillas HTML y Estilos CSS (`templates/`)](#4-plantillas-html-y-estilos-css-templates)
  - [A. Vista Animes (`post_animes.html`)](#a-vista-animes-post_animeshtml)
  - [B. Vista Disponibilidad (`post_disponibilidad.html`)](#b-vista-disponibilidad-post_disponibilidadhtml)
  - [C. Vista Plataformas (`post_plataformas.html`)](#c-vista-plataformas-post_plataformashtml)

---

## 1. Modelos de Datos (`models.py`)


Definición de las clases de la base de datos para registrar usuarios cuidadores, especies de animales, organizaciones protectoras y sus colaboradores:

Definición de las clases que estructuran la base de datos del 

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

# Modelo Anime 
class Anime(models.Model):
    titulo = models.CharField(max_length=150)
    titulo_original = models.CharField(max_length=150)
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


---

## 2. Configuración de Rutas (`urls.py`)

adores:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('animales/', views.mostrar_animales, name='post_animales'),
    path('protectoras/', views.mostrar_protetcoras, name='post_protectoras'),
    path('colaboradores/', views.mostrar_colaboradores, 
    path('animes/', views.mostrar_animes, name='post_animes'),
    path('plataformas/', views.mostrar_plataformas, name='post_plataformas'),
    path('disponibilidad/', views.mostrar_disponibilidad, 
]
```

---

## 3. Controladores y Vistas (`views.py`)


Funciones encagadas de obtener los registros de la base de datos y pasarlos al contexto de las plantillas HTML:

```python
from django.shortcuts import render
from .models import Animal, Protectora, ColaboradorLógica encagada de consultar la base de datos y renderizar las plantillas correspondientes:

```python
from django.shortcuts import render


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
def mostrar_animes(request):
    posts = Anime.objects.all()
    return render(request, 'post_animes.html', {'mostrar_post_animes': posts})

def mostrar_plataformas(request):
    post = Plataforma.objects.all()
    return render(request, 'post_plataformas.html', {'mostrar_post_plataformas': post}) 

def mostrar_disponibilidad(request):
    post = Disponibilidad.objects.all()
    return render(request, 'post_disponibilidad.html', {'mostrar_post_disponibilidad': post}) 

```

---

## 4. Plantillas HTML y Estilos CSS (`templates/`)


### Vista Colaboradores (`post_colaboradores.html`)

Muestra el listado de colaboradores con sus nombres y cargos desempeñados dentro de la protectora, usando estilos adaptados en verde esmeralda.

### A. Vista Animes (`post_animes.html`)


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
    <table class="tabla-animes">
        <thead>
            <tr>
                <th>Titulo</th>
                <th>Numero de episodios</th>
                <th>Imagen</th>
            </tr>
        </thead>
        <tbody>
            {% for animes in mostrar_post_animes %}
            <tr>
                <td>{{ animes.titulo }}</td>
                <td><strong>{{ animes.num_episodios }}</strong></td>
                <td class="imagen">
                    <img src="{{ animes.imagen.url }}" alt="{{ animes.titulo }}">
                </td>            

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

    .tabla-animes {

        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        border-radius: 8px 8px 0 0;
        overflow: hidden;
    }

    .tabla-colaboradores thead tr {

    .tabla-animes thead tr {

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

    .tabla-animes th, .tabla-animes td {
        padding: 12px 15px;
    }
    .tabla-animes tbody tr {
        border-bottom: 1px solid #dddddd;
    }
    .tabla-animes tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
    .tabla-animes tbody tr:last-of-type {
        border-bottom: 2px solid #009879;
    }
    .regreso a {
        color: #008000;
    }
    .tabla-animes .imagen img {
        width: 120px;
        height: 170px;
        object-fit: cover;
    }
</style>
```

---

### B. Vista Disponibilidad (`post_disponibilidad.html`)

```html
<main class="contenedor">
    <!-- Tabla Estilizada -->
    <table class="tabla-disponibilidad">
        <thead>
            <tr>
                <th>Idioma del audio</th>
                <th>Doblaje</th>
                <th>Activo</th>
            </tr>
        </thead>
        <tbody>
            {% for disponibilidad in mostrar_post_disponibilidad %}
            <tr>
                <td>{{ disponibilidad.idioma_audio }}</td>
                <td><strong>{{ disponibilidad.doblaje }}</strong></td>
                <td>{{ disponibilidad.activo }}</td>
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
    .tabla-disponibilidad {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        border-radius: 8px 8px 0 0;
        overflow: hidden;
    }
    .tabla-disponibilidad thead tr {
        background-color: #009879;
        color: #ffffff;
        text-align: left;
        font-weight: bold;
    }
    .tabla-disponibilidad th, .tabla-disponibilidad td {
        padding: 12px 15px;
    }
    .tabla-disponibilidad tbody tr {
        border-bottom: 1px solid #dddddd;
    }
    .tabla-disponibilidad tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
    .tabla-disponibilidad tbody tr:last-of-type {

        border-bottom: 2px solid #009879;
    }
    .regreso a {
        color: #008000;
    }
</style>


---

### C. Vista Plataformas (`post_plataformas.html`)

```html
<main class="contenedor">
    <!-- Tabla Estilizada -->
    <table class="tabla-plataformas">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Web</th>
                <th>Logo</th>
            </tr>
        </thead>
        <tbody>
            {% for plataformas in mostrar_post_plataformas %}
            <tr>
                <td>{{ plataformas.nombre }}</td>
                <td>
                    <a href="{{ plataformas.web }}" target="_blank">
                        Visitar Web
                    </a>
                </td>
                <td class="imagen">
                    <img src="{{ plataformas.logo.url }}" alt="{{ plataformas.nombre }}">
                </td>    
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
    .tabla-plataformas {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        border-radius: 8px 8px 0 0;
        overflow: hidden;
    }
    .tabla-plataformas thead tr {
        background-color: #009879;
        color: #ffffff;
        text-align: left;
        font-weight: bold;
    }
    .tabla-plataformas th, .tabla-plataformas td {
        padding: 12px 15px;
    }
    .tabla-plataformas tbody tr {
        border-bottom: 1px solid #dddddd;
    }
    .tabla-plataformas tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
    .tabla-plataformas tbody tr:last-of-type {
        border-bottom: 2px solid #009879;
    }
    .regreso a {
        color: #008000;
    }
    .tabla-plataformas .imagen img {
        width: 120px;
        height: 170px;
        object-fit: cover;
    }
</style>
