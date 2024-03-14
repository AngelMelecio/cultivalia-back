from django.db import models
from backend.constants.base import *
from apps.DetalleVenta.models import DetalleVenta
from apps.Predio.models import Predio

CONTRATOS_PATH = 'archivos/contratos/'

ESTADO_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('Vigente', 'Vigente'),
    ('Cancelado', 'Cancelado'),
]

TIPO_CHOICES = [
    ('Compra','Compra')
]

class Contrato(models.Model):
    idContrato = models.AutoField(auto_created=True, primary_key=True)
    predio = models.ForeignKey(Predio, on_delete=models.RESTRICT, **NOT_NULL)
    detalleVenta = models.OneToOneField(DetalleVenta, on_delete=models.CASCADE)
    folio = models.IntegerField(unique=True)
    tipo = models.CharField(max_length=45, choices=TIPO_CHOICES, default='Compra')
    archivo = models.FileField(upload_to=CONTRATOS_PATH)
    estado = models.CharField(max_length=45, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f'{self.folio}'