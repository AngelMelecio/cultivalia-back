from rest_framework import serializers
 
from apps.Administrador.models import Administrador
 

class AdministradorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Administrador
        fields = '__all__'