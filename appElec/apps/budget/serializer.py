from rest_framework import serializers
from .models import Budgets, Items, BudgetItems, Clients


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "mount": instance.mount,
            "material": instance.material.description,
        }



class BudgetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budgets
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "code": instance.code,
            "owner": instance.owner.name,
            "items": ItemsSerializer(instance.items.all(), many=True).data,
        }
