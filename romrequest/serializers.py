from rest_framework import serializers
from .models import RomRequest, Employees, CEmployees

class RomRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RomRequest
        fields = '__all__'
