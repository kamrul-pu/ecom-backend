"""Serializer for OrderItem model."""

from rest_framework import serializers

from order.models import OrderItem


class OrderItemBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "uid",
            "product",
            "product_name",
        )
        read_only_fields = (
            "id",
            "uid",
            "product_name",
        )


class OrderItemListSerializer(OrderItemBaseSerializer):
    class Meta(OrderItemBaseSerializer.Meta):
        fields = OrderItemBaseSerializer.Meta.fields + (
            "quantity",
            "price",
            "total",
        )
        read_only_fields = OrderItemBaseSerializer.Meta.read_only_fields + (
            "price",
            "total",
        )

    # def create(self, validated_data):
    #     user = self.context.get("request").user
    #     validated_data["entry_by_id"] = user.id
    #     return super().create(validated_data)
