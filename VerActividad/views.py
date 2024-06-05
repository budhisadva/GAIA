from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Publicar.models import Post
from SolicitudAmistad.models import Amistad

@login_required
def index(request):
    amigos = Amistad.objects.filter(Q(emisor=request.user) | Q(receptor=request.user)).exclude(aceptada=False)
    post_amigos = amigos.values_list('receptor', flat=True).union(amigos.values_list('emisor', flat=True))
    posts = Post.objects.filter(usuario__in=post_amigos).order_by('-fecha_creacion')
    return render(request, 'VerActividad.html', {
        'posts': posts,
        'amigos': amigos,
    })
