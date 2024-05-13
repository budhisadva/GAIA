from django.urls import path
from . import views

app_name = 'VerActividad'

urlpatterns = [
    path('', views.index, name='index'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
]
