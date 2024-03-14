from django.db import models
from backend.constants.base import *
from apps.Predio.models import Predio

class Jima(models.Model):
    idJima = models.AutoField(auto_created=True, primary_key=True)
    fecha = models.DateField(**NOT_NULL)
    precioKilo = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL)
    pesoPromedioPlanta = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL)
    predio = models.ForeignKey(Predio, on_delete=models.PROTECT, **NOT_NULL)
    
    def __str__(self):
        return f'{self.fecha} - {self.predio}'