from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'CrearCuenta.html')

def crearCuenta(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Se ha enviado un mensaje de confirmacion a tu correo'))
            return HttpResponseRedirect('/verActividad')
        else:
            messages.success(request, ('Hubo un error al crear tu cuenta. Intenta de nuevo.'))
            return HttpResponseRedirect('/crearCuenta')
    else:
        formulario = request.POST.dict()
        print(formulario)
    return HttpResponseRedirect('/verActividad')
