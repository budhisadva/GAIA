from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def base(request):
    users = User.objects.all().exclude(id=request.user.id)
    return render(request, 'Administracion.html', {
        'usuarios': users
    })

def bloquear(request, usr_id):
    user = User.objects.get(id=usr_id)
    user.is_active = False
    user.save()
    return redirect('Administracion:base')

def desbloquear(request, usr_id):
    user = User.objects.get(id=usr_id)
    user.is_active = True
    user.save()
    return redirect('Administracion:base')

def eliminar(request, usr_id):
    user = User.objects.get(id=usr_id)
    user.delete()
    return redirect('Administracion:base')
