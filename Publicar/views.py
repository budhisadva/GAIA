from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Publicar.models import PublicarForm # modelo donde guardare la publicacion

def publicar(request):
    print("Aqui voy a guardar las publicaciones ")
    print (request.POST['texto'])
    publicacion = PublicarForm(texto=request.POST['texto'])
    publicacion.save()
    # regreso a ver actividad despues de publicar 
    return HttpResponseRedirect('/verActividad')
# Create your views here.
def index(request):
    return HttpResponse('Publicar')

