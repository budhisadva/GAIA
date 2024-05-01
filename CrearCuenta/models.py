from django.db import models

# Create your models here.

class Usuario(models.Model):
    #idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=50)
    fecha = models.DateField()
    genero = models.CharField(max_length=20)
    #esadmin, models.BooleanField()

    def __str__(self):
        return self.nombre
