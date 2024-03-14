from django.db import models
from backend.constants.base import *

class Beneficiario(models.Model):
    idBeneficiario = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=45, **NOT_NULL)
    primerApellido = models.CharField(max_length=45, **NOT_NULL)
    segundoApellido = models.CharField(max_length=45, blank=True, null=True)
    sexo = models.CharField( max_length=20, choices=SEXO_CHOICES, **NOT_NULL)
    parentesco = models.CharField(max_length=45, **NOT_NULL)

    def __str__(self):
        return f'{self.nombre} {self.primerApellido} {self.segundoApellido}'