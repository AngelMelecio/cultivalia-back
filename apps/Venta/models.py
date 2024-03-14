from django.db import models
from backend.constants.base import *
from apps.Inversor.models import Inversor
from apps.Usuario.models import Usuario
from apps.Inversor.models import Inversor

class Venta(models.Model):
    idVenta = models.AutoField(auto_created=True, primary_key=True)
    supervisor = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    comprador = models.ForeignKey(Inversor, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True, **NOT_NULL)

    def __str__(self):
        return f'{self.supervisor} - {self.comprador} - {self.fecha}'