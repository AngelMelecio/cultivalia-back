from rest_framework import serializers
 
from apps.Inversor.models import Inversor
 

class InversorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Inversor
        fields = '__all__'