from rest_framework import serializers
 
from apps.Asesor.models import Asesor
 

class AsesorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Asesor
        fields = '__all__'