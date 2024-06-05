from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Amistad(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emisor", null=True)
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receptor", null=True)
    aceptada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.emisor} y {self.receptor}"
