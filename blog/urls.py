from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animes/', views.mostrar_animes, name='post_animes'),
    path('plataformas/', views.mostrar_plataformas, name='post_plataformas'),
    path('disponibilidad/', views.mostrar_disponibilidad, name='post_disponibilidad'),
]
