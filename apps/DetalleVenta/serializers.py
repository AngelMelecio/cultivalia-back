from rest_framework import serializers
 
from apps.DetalleVenta.models import DetalleVenta
 

class DetalleVentaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = DetalleVenta
        fields = '__all__'