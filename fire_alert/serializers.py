from rest_framework import serializers
from .models import FireAlert

class FireAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireAlert
        fields = ['img', 'isFire', 'timestamp', 'user']