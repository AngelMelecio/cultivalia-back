from django.db import models
from backend.constants.base import *
from django.contrib.auth.models import AbstractUser

ROL_CHOICES = [
    ('SuperAdmin', 'SuperAdmin'),
    ('Administrador', 'Administrador'),
    ('Inversor', 'Inversor'),
]

class Usuario(AbstractUser):
    
    first_name = models.CharField( max_length=45, blank=True)
    last_name = models.CharField( max_length=45, blank=True)
    
    email = models.EmailField(max_length=45, unique=True, **NOT_NULL)
    
    tipo = models.CharField(choices=ROL_CHOICES, max_length=45, blank=True )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'