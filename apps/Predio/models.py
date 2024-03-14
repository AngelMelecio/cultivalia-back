from django.db import models
from backend.constants.base import *

class Predio(models.Model):
    idPredio = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=45, **NOT_NULL)
    coordenadas = models.CharField(max_length=45, **NOT_NULL)
    imagen = models.ImageField(upload_to=f'{IMAGENES_PATH}predios/', blank=True, null=True)
    fechaSiembra = models.DateField()
    plantas = models.IntegerField()
    hectareas = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL)

    def __str__(self):
        return f'{self.nombre}'