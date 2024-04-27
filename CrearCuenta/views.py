from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'CrearCuenta.html')

def crearCuenta(request):
    print(request.POST.dict())
    return HttpResponseRedirect('/verActividad')
