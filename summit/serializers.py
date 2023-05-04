from rest_framework import serializers
from .models import SummitData

class SummitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummitData
        fields = '__all__'
