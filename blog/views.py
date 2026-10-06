from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# Create your views here.
def index(request):
    return render (request, 'index.html')

def mostrar_animales(request):
    posts = Animal.objects.all()
    return render(request, 'post_animales.html', {'mostrar_post_anaimales' : posts})

def mostrar_protetcoras(request):
    post = Protectora.objects.all()
    return render(request, 'post_protectoras.html' , { 'mostrar_post_protectoras' : post}) 

def mostrar_colaboradores(request):
    post = Colaborador.objects.all()
    return render(request, 'post_colaboradores.html' , { 'mostrar_post_colaboradores' : post}) 

