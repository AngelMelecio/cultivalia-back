from django.db import models
from backend.constants.base import *
from apps.Usuario.models import Usuario
from apps.Perfil.models import Perfil

class Administrador(models.Model):
    idAdministrador = models.AutoField(auto_created=True, primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, **NOT_NULL)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, **NOT_NULL)

    def __str__(self):
        return f'{self.perfil.nombre} {self.perfil.apellidos}'