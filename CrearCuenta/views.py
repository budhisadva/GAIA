from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from django.contrib import messages
from . import models

# Create your views here.
def index(request):
    return render(request, 'CrearCuenta.html')

def crear(request):
    if request.method == 'POST':
        formulario = request.POST.dict()
        try:
            user = User.objects.create_user(username=formulario['nombre'],
                                            email=formulario['correo'],
                                            password=formulario['contrasena'])
            user.save()
            usuario = models.Usuario(usuario=user,
                                     genero=formulario['genero'],
                                     fechaN=formulario['fecha'])
            usuario.save()
            login(request, user)
            return redirect('VerActividad:index')
        except IntegrityError:
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect('CrearCuenta:index')
        except Exception as e:
            print(e)
            messages.error(request, f"{e}")
            return redirect('CrearCuenta:index')
    else:
        return redirect("CrearCuenta:index")
