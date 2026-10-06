from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animales/', views.mostrar_animales, name='post_animales'),
    path('protectoras/', views.mostrar_protetcoras, name='post_protectoras'),
    path('colaboradores/', views.mostrar_colaboradores, name='post_colaboradores'),
]
