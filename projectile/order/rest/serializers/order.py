"""Serializer for Order model."""

from rest_framework import serializers

from order.models import Order
from order.rest.serializers.order_item import (
    OrderItemListSerializer,
)


class OrderBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "uid",
            "customer",
            "delivery_date",
            "payment_method",
            "payment_status",
            "order_status",
        )
        read_only_fields = (
            "id",
            "uid",
            "customer",
            "delivery_date",
        )


class OrderListSerializer(OrderBaseSerializer):
    order_items = OrderItemListSerializer(read_only=True)

    class Meta(OrderBaseSerializer.Meta):
        fields = OrderBaseSerializer.Meta.fields + ("order_items",)
        read_only_fields = OrderBaseSerializer.Meta.read_only_fields + (
            "order_total",
            "additional_discount",
            "grand_total",
        )

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["entry_by_id"] = user.id
        return super().create(validated_data)
