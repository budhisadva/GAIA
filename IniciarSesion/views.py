from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
            return render(request, 'IniciarSesion.html', {
                'error': 'Nombre o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('VerActividad:index')
