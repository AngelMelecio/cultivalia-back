from django.db import models
from backend.constants.base import *
from apps.Venta.models import Venta
from apps.Oferta.models import Oferta

class DetalleVenta(models.Model):
    idDetalleVenta = models.AutoField(auto_created=True, primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.RESTRICT)
    oferta = models.ForeignKey(Oferta, on_delete=models.RESTRICT)
    precioPlanta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.venta} - {self.oferta}'