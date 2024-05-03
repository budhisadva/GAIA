from django.db import models

class PublicarForm(models.Model):
    #guardo el texto 
    texto = models.TextField(max_length=500)
   # foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    #video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.texto

    # Puedes agregar validaciones adicionales aquí si es necesario


