from rest_framework import serializers
from .models import MobileToken


class MobileTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileToken
        fields = "__all__"
