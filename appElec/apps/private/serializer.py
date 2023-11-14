from rest_framework import serializers
from apps.public.models import Menssage

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menssage
        fields = '__all__'