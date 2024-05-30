from django.urls import path
from . import views

app_name = 'CerrarSesion'

urlpatterns = [
    path('', views.cerrar_sesion, name='cerrar_sesion'),
]
