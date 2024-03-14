from django.db import models
from backend.constants.base import *
from apps.Inversor.models import Inversor

COMPROBANTES_PATH = 'archivos/comprobantes/'

TIPO_OPERACION_CHOICES = [
    ('Fondeo', 'Fondeo'),
    ('Retiro', 'Retiro'),
]

class Operacion(models.Model):
    idOperacion = models.AutoField(auto_created=True, primary_key=True)
    inversor = models.ForeignKey(Inversor, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True, **NOT_NULL)
    tipo = models.CharField(choices=TIPO_OPERACION_CHOICES, max_length=45, **NOT_NULL)
    monto = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL)
    metodo = models.CharField(max_length=45)
    comentarios = models.TextField()
    comprobante = models.FileField(upload_to=COMPROBANTES_PATH, blank=True, null=True)

    def __str__(self):
        return f'{self.inversor} - {self.tipo} - {self.monto}'
