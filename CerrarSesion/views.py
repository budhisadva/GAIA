from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def cerrar_sesion(request):
    logout(request)
    return redirect('IniciarSesion:index')
