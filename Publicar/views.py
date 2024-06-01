from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def crear(request):
    if request.method == 'POST':
        if request.POST['texto']:
            post = Post(
                usuario = request.user,
                texto = request.POST['texto']
            )
            post.save()
            if request.POST['enlace']:
                post.enlace = request.POST['enlace']
                post.save()
            if request.FILES.get('foto'):
                post.imagen = request.FILES['foto']
                post.save()
    return redirect('VerActividad:index')
