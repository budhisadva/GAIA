from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario

# login_usuario
def index(request):
    if request.method == "POST":
        email = request.POST['correo']
        password = request.POST['contrasena']
        user = authenticate(request, correo=email, contrasena=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Se ha iniciado la sesion"))
            return redirect('/verActividad')
        else:
            messages.success(request, ("Hubo un error al iniciar sesion. Intente nuevamente"))
            return redirect('/publicar')
    else:
        return render(request, 'IniciarSesion.html')

def logout_usuario(request):
    logout(request)
    messages.success(request, ("Se ha cerrado la sesion"))
    return redirect('IniciarSesion.html')
