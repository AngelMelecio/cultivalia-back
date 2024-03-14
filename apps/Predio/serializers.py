from rest_framework import serializers
 
from apps.Predio.models import Predio
 

class PredioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Predio
        fields = '__all__'