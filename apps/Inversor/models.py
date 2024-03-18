from django.db import models
from django.utils import timezone
from backend.constants.base import *
from apps.Asesor.models import Asesor
from apps.Beneficiario.models import Beneficiario
from apps.Usuario.models import Usuario

class Inversor(models.Model):
    idInversor = models.AutoField(auto_created=True, primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, **NOT_NULL)
    
    fechaNacimiento = models.DateField(blank=True, default=timezone.now) 
    sexo = models.CharField( max_length=20, choices=SEXO_CHOICES, **NOT_NULL, default='Masculino')
    nacionalidad = models.CharField(max_length=45, blank=True)
    telefono = models.CharField(max_length=45, blank=True)

    tipoIdentificacion = models.CharField(max_length=45, **NOT_NULL)
    numeroIdentificacion = models.CharField(max_length=45, **NOT_NULL)
    credencial = models.ImageField(upload_to=f'{IMAGENES_PATH}credenciales/', **NOT_NULL)

    direccion = models.CharField(max_length=45, **NOT_NULL)
    colonia = models.CharField(max_length=45, **NOT_NULL)
    ciudad = models.CharField(max_length=45, **NOT_NULL)
    codigoPostal = models.CharField(max_length=10, **NOT_NULL)
    estado = models.CharField(max_length=45, **NOT_NULL)
    pais = models.CharField(max_length=45, **NOT_NULL)
    
    dineroDisponible = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL)
    
    # quitar
    dineroInvertido = models.DecimalField(max_digits=10, decimal_places=2, **NOT_NULL) # Ask Cesar
    
    asesor = models.ForeignKey(Asesor, on_delete=models.PROTECT)
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.PROTECT)
    codigoReferido = models.OneToOneField('CodigoReferido.CodigoReferido', on_delete=models.SET_NULL, blank=True, null=True, related_name='codigo_referido') 
    firstTime = models.BooleanField(**NOT_NULL, default=True)


    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}'