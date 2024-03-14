from rest_framework import serializers
 
from apps.Oferta.models import Oferta
 

class OfertaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Oferta
        fields = '__all__'