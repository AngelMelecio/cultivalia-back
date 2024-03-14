from rest_framework import serializers
 
from apps.CodigoReferido.models import CodigoReferido
 

class CodigoReferidoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CodigoReferido
        fields = '__all__'