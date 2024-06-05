from django.urls import path
from . import views

app_name = 'SolicitudAmistad'

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('enviar/<int:receptor>/', views.enviar, name='enviar'),
    path('notificaciones/', views.notificaciones, name='notificaciones'),
    path('aceptar/<int:solicitud_id>/', views.aceptar, name='aceptar'),
]
