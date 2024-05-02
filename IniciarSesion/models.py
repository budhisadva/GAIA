from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo = models.EmailField()
    contrasena = models.CharField(max_length=50)
