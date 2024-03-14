from django.db import models
from backend.constants.base import *

class Asesor(models.Model):
    idAsesor = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=45, **NOT_NULL)
    apellidos = models.CharField(max_length=45, **NOT_NULL)
    telefono = models.CharField(max_length=45, **NOT_NULL)
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos}'