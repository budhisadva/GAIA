from django.urls import path
from . import views

app_name = 'ActualizarCuenta'

urlpatterns = [
    path('', views.index, name='index'),
    path('nombre/', views.nombre, name='nombre'),
    path('contrasena/', views.nombre, name='contrasena'),
    path('correo/', views.nombre, name='correo'),
]
