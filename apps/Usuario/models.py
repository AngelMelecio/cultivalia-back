from django.db import models
from backend.constants.base import *
from django.contrib.auth.models import AbstractUser

ROL_CHOICES = [
    ('SuperAdmin', 'SuperAdmin'),
    ('Administrador', 'Administrador'),
    ('Inversor', 'Inversor'),
]

class Usuario(AbstractUser):
    correo = models.CharField(max_length=45, **NOT_NULL)
    telefono = models.CharField(max_length=45, **NOT_NULL)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    tipo = models.CharField(choices=ROL_CHOICES, max_length=45, **NOT_NULL)
    
    def __str__(self):
        return f'{self.nombreUsuario}'