from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from Publicar.models import Post

@login_required
def index(request):
    posts = Post.objects.filter(usuario=request.user)
    return render(request, 'VerActividad.html', {
        'posts': posts
    })
