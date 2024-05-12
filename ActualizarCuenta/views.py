from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'ActualizarCuenta.html')

#
def nombre(request):
    form = request.POST.dict()
    print(form)
    return HttpResponseRedirect('/actualizarCuenta')

#
def contrasena(request):
    form = request.POST.dict()
    print(form)
    return HttpResponseRedirect('/actualizarCuenta')

#
def correo(request):
    form = request.POST.dict()
    print(form)
    return HttpResponseRedirect('/actualizarCuenta')
