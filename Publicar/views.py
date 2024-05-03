from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Publicar.models import PublicarForm  # Asegúrate de importar el formulario correcto.

def publicar(request):
    print("Aqui voy a guardar las publicaciones ")
    print (request.POST['texto'])
    # regreso a ver actividad despues de publicar 
    return HttpResponseRedirect('/verActividad')
# Create your views here.
def index(request):
    return HttpResponse('Publicar')

