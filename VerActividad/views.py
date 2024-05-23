from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'VerActividad.html')

#
def publicaciones(request):
    publicaciones = {'post': []}
    return JsonResponse(publicaciones)
