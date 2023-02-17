from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from item.models import Item


class CreateItemSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        validators = [UniqueValidator(queryset = Item.objects.all(), message = "item name already existy")]
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "create_at"
        ]
        read_only_fields = ["id", "create_at"]

class ListItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "create_at"
        ]
        read_only_fields = ["id", "create_at"]