from rest_framework import serializers
from .models import Budgets, Items


class BudgetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budgets
        fields = "__all__"


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"