from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'IniciarSesion.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = request.POST.dict()
        user = authenticate(request,
                            username=formulario['nombre'],
                            password=formulario['contrasena'])
        if user is None:
            messages.error(request, "Nombre y/o contraseña incorrectas.")
            return redirect('IniciarSesion:index')
        else:
            login(request, user)
            return redirect('VerActividad:index')
