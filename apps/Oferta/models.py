from django.db import models
from backend.constants.base import *
from apps.Inversor.models import Inversor
from apps.Predio.models import Predio

ESTADO_OFERTA_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('Vigente', 'Vigente'),
    ('Aceptada', 'Aceptada'),
    ('Rechazada', 'Rechazada'),
    ('Finalizada', 'Finalizada'),
]

TIPO_OFERTA_CHOICES = [
    ('Pública', 'Pública'),
    ('Privada', 'Privada'),
]

class Oferta(models.Model):
    idOferta = models.AutoField(auto_created=True, primary_key=True)
    cantidadPlantas = models.IntegerField(**NOT_NULL)
    precioPlanta = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL)
    fechaCreacion = models.DateTimeField(auto_now_add=True, **NOT_NULL)
    vendedor = models.ForeignKey(Inversor, on_delete=models.PROTECT)
    predio = models.ForeignKey(Predio, on_delete=models.PROTECT, **NOT_NULL)
    estado = models.CharField(choices=ESTADO_OFERTA_CHOICES, max_length=45, **NOT_NULL)
    tipo = models.CharField(choices=TIPO_OFERTA_CHOICES, max_length=45, **NOT_NULL)

    def __str__(self):
        return f'{self.vendedor} - {self.predio} - {self.estado}'