from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Publicar.models import PublicarForm # modelo donde guardare la publicacion

def publicar(request):
    print("Aqui voy a guardar las publicaciones ")
    if request.method == 'POST':
        # Obtener los datos del formulario
        texto = request.POST['texto']
        foto = request.FILES.get('foto')
        publicacion = PublicarForm(texto=texto, foto=foto)
        publicacion.save()
        if foto:
            print("Nombre de la foto:", foto.name)
            print("Tipo de archivo:", foto.content_type)
            print("Tamaño de la foto:", foto.size)

    print (request.POST['texto'])
    #publicacion = PublicarForm(texto=request.POST['texto'])
    #publicacion.save()
    # regreso a ver actividad despues de publicar 
    return HttpResponseRedirect('/verActividad')
# Create your views here.
def index(request):
    return HttpResponse('Publicar')

