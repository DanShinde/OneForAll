from rest_framework import serializers
from .models import SummitData
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


# class SummitDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SummitData
#         fields = '__all__'

class SummitDataSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SummitData
        fields = '__all__'
