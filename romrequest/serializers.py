from rest_framework import serializers
from .models import WebApp

class WebAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebApp
        fields = '__all__'