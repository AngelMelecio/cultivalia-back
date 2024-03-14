from rest_framework import serializers
 
from apps.Jima.models import Jima
 

class JimaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Jima
        fields = '__all__'