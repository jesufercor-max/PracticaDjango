from django.shortcuts import render
from .models import Anime, Plataforma, Disponibilidad

# Create your views here.
def index(request):
    return render (request, 'index.html')

def mostrar_animes(request):
    posts = Anime.objects.all()
    return render(request, 'post_animes.html', {'mostrar_post_animes' : posts})

def mostrar_plataformas(request):
    post = Plataforma.objects.all()
    return render(request, 'post_plataformas.html' , { 'mostrar_post_plataformas' : post}) 

def mostrar_disponibilidad(request):
    post = Disponibilidad.objects.all()
    return render(request, 'post_disponibilidad.html' , { 'mostrar_post_disponibilidad' : post}) 

