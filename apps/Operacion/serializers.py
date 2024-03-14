from rest_framework import serializers
 
from apps.Operacion.models import Operacion
 

class OperacionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Operacion
        fields = '__all__'