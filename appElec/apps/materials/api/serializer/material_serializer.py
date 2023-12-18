from rest_framework import serializers
from ...models import Materials


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = [
            "id",
            "tag",
            "description",
            "unit",
            "price",
            "provider",
        ]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "tag": instance.tag.name,
            "description": instance.description,
            "unit": instance.get_unit_display(),
            "price": instance.price,
            "provider": instance.provider.name
        }