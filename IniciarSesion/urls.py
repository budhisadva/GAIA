from django.urls import path
from . import views

app_name = 'IniciarSesion'

urlpatterns = [
    path('', views.index, name='index'),
    path('ingresar', views.iniciar_sesion, name='iniciar_sesion'),
]
