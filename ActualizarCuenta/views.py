from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login

@login_required
def index(request):
    return render(request, 'ActualizarCuenta.html')

@login_required
def nombre(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=request.user.id)
            user.username = request.POST['nombre']
            user.save()
        except IntegrityError:
            messages.error(request, f"El nombre: {request.POST['nombre']}, no está disponible")
            return redirect('ActualizarCuenta:index')
        except Exception as e:
            print(e)
            messages.error(request, f"{e}")
            return redirect('ActualizarCuenta:index')
        messages.success(request, 'Nombre actualizado correctamente.')
        return redirect('ActualizarCuenta:index')

@login_required
def contrasena(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.password = make_password(request.POST['contrasena'])
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Contraseña actualizada correctamente.')
        return redirect('ActualizarCuenta:index')

@login_required
def correo(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.email = request.POST['correo']
        user.save()
        messages.success(request, 'Correo actualizado correctamente.')
        return redirect('ActualizarCuenta:index')

@login_required
def super(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        if request.POST.get('superUsuario') is None:
            user.is_superuser = False
        else:
            user.is_superuser = True
        user.save()
        messages.success(request, 'Estado de cuenta actualizado correctamente.')
        return redirect('ActualizarCuenta:index')
