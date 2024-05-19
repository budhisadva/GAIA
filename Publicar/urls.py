from django.urls import path
from . import views

app_name = 'Publicar'

urlpatterns = [
    path('crear/', views.crear, name='crear')
]
