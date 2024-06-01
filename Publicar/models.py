from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    imagen = models.ImageField(default='null', upload_to='posts')
    enlace = models.URLField(max_length=200, default='null')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
