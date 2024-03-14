from django.db import models
from backend.constants.base import *
from apps.Inversor.models import Inversor

class Cuenta(models.Model):
    idCuenta = models.AutoField(auto_created=True, primary_key=True)
    titular = models.CharField(max_length=45, **NOT_NULL)
    banco = models.CharField(max_length=45, **NOT_NULL)
    clabe = models.CharField(max_length=45, **NOT_NULL)
    inversor = models.ForeignKey(Inversor, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.banco} - {self.titular}'