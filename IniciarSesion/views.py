from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'IniciarSesion.html')

def ingresar(request):
    formulario = request.POST.dict()
    print(formulario)
    return HttpResponseRedirect('/verActividad')
