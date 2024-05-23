from django.shortcuts import render
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
        user = User.objects.get(id=request.user.id)
        user.username = request.POST['nombre']
        user.save()
        return render(request, 'ActualizarCuenta.html', {
            'mensaje': 'Nombre actualizado correctamente'
        })

@login_required
def contrasena(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.password = make_password(request.POST['contrasena'])
        user.save()
        update_session_auth_hash(request, user)
        return render(request, 'ActualizarCuenta.html', {
            'mensaje': 'Contraseña actualizada correctamente'
        })

@login_required
def correo(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.email = request.POST['correo']
        user.save()
        return render(request, 'ActualizarCuenta.html', {
            'mensaje': 'Correo actualizado correctamente'
        })
