from django.db import models
from backend.constants.base import *        

class Perfil(models.Model):
    idPerfil = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=45, **NOT_NULL)
    apellidos = models.CharField(max_length=45, **NOT_NULL)
    fechaNacimiento = models.DateField(**NOT_NULL) 
    sexo = models.CharField( max_length=20, choices=SEXO_CHOICES, **NOT_NULL)
    nacionalidad = models.CharField(max_length=45, **NOT_NULL)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'