from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from . import models

# Create your views here.
def index(request):
    return render(request, 'CrearCuenta.html')

def crearCuenta(request):
    if request.method == 'POST':
        formulario = request.POST.dict()
        try:
            user = User.objects.create_user(username=formulario['nombre'],
                                            email=formulario['correo'],
                                            password=formulario['contrasena'])
            user.save()
            login(request, user)
            usuario = models.Usuario(usuario=user,
                                     genero=formulario['genero'],
                                     fechaN=formulario['fecha'])
            usuario.save()
            return redirect('VerActividad:index')
        except Exception as e:
            return render(request, 'CrearCuenta.html', {
                'error': f'Error: {e}'
            })
