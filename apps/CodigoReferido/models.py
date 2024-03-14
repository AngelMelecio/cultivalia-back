from django.db import models
from backend.constants.base import *
from django.utils.crypto import get_random_string

class CodigoReferido(models.Model):
    idCodigoReferido = models.AutoField(auto_created=True, primary_key=True)
    codigo = models.CharField(max_length=6, unique=True)
    inversor = models.OneToOneField('Inversor.Inversor', on_delete=models.CASCADE, related_name='propietario')

    def __str__(self):
        return f'{self.codigo}'

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = CodigoReferido.generate_unique_code()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_code():
        length = 6
        # Define a string of allowed characters, excluding easily confused ones like 'I', 'l', '0', 'O'
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        while True:
            code = get_random_string(length=length, allowed_chars=allowed_chars)
            if not CodigoReferido.objects.filter(codigo=code).exists():
                break
        return code