from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def crear(request):
    formulario = request.POST.dict()
    print(formulario)
    return HttpResponseRedirect('/verActividad')
