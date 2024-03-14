from rest_framework import serializers
 
from apps.Beneficiario.models import Beneficiario
 

class BeneficiarioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Beneficiario
        fields = '__all__'