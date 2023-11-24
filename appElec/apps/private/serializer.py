from rest_framework import serializers
from apps.public.models import Menssage
from .models import MobileToken

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menssage
        fields = '__all__'

class MobileTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileToken
        fields = '__all__'