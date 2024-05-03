from django.urls import path
from . import views
#from .models import

urlpatterns = [
    #path('', views.index, name='publicar'),
    path('verActividad/', views.publicar, name='publicar'),
]
