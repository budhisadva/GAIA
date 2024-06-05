from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from SolicitudAmistad.models import Amistad

def usuarios(request):
    datos = {'usuarios': []}
    solicitudesEnviadas = []
    solicitudesAceptadas = []
    # obtener lista de todos los usuarios a los que se les ha enviado solicitud
    for amistad in Amistad.objects.filter(aceptada=False, emisor=request.user):
        solicitudesEnviadas.append(amistad.receptor)
    # obtenr lista de amigos del usuario
    for amistad in Amistad.objects.filter(Q(emisor=request.user) | Q(receptor=request.user)).exclude(aceptada=False):
        solicitudesAceptadas.append(amistad.receptor)
        solicitudesAceptadas.append(amistad.emisor)
    solicitudesAceptadas = list(set(solicitudesAceptadas))
    try:
        solicitudesAceptadas.remove(request.user)
    except Exception as e:
        pass
    # obtener lista de todos los usuarios y enviarla en formato JSON
    users = User.objects.all().exclude(id=request.user.id)
    for user in users:
        if user not in solicitudesAceptadas:
            if user in solicitudesEnviadas:
                datos['usuarios'].append({'id': user.id, 'nombre': user.username, 'enviada':True})
            else:
                datos['usuarios'].append({'id': user.id, 'nombre': user.username, 'enviada':False})
    return JsonResponse(datos)

def enviar(request, receptor):
    enviar_a = User.objects.get(id=receptor)
    enviado_de = User.objects.get(id=request.user.id)
    amistad = Amistad(emisor=enviado_de,
                      receptor=enviar_a)
    amistad.save()
    return redirect('VerActividad:index')

def notificaciones(request):
    solicitudes = Amistad.objects.filter(receptor=request.user, aceptada=False)
    return render(request, 'Solicitudes.html', {
        'solicitudes': solicitudes
    })

def aceptar(request, solicitud_id):
    amistad = Amistad.objects.get(pk=solicitud_id)
    amistad.aceptada = True
    amistad.save()
    return redirect('SolicitudAmistad:notificaciones')
