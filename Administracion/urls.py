from django.urls import path
from . import views

app_name = 'Administracion'

urlpatterns = [
    path('base/', views.base, name='base'),
    path('bloquear/<int:usr_id>/', views.bloquear, name='bloquear'),
    path('desbloquear/<int:usr_id>/', views.desbloquear, name='desbloquear'),
    path('eliminar/<int:usr_id>/', views.eliminar, name='eliminar'),
]
