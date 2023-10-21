from django.db import models

class Image(models.Model):
    nombre = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.nombre