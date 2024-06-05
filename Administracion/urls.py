from django.urls import path
from . import views

app_name = 'Administracion'

urlpatterns = [
    path('base/', views.base, name='base'),
]
