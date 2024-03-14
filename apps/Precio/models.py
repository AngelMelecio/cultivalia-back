from django.db import models
from backend.constants.base import *

class Precio(models.Model):
    idPrecio = models.AutoField(auto_created=True, primary_key=True)
    fecha = models.DateField(**NOT_NULL)
    precioAnterior = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL)
    precioActual = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL)
    
    def __str__(self):
        return f'{self.fecha} - {self.precioActual}'