from rest_framework import serializers
from apps.public.models import Message
from .models import MobileToken


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class MobileTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileToken
        fields = "__all__"
