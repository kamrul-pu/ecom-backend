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
    order_items = OrderItemListSerializer(read_only=True, many=True)

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


class AdminOrderListSerializer(OrderBaseSerializer):
    class Meta(OrderBaseSerializer.Meta):
        fields = OrderBaseSerializer.Meta.fields + (
            "complete",
            "order_total",
            "additional_discount",
            "grand_total",
        )
        read_only_fields = OrderBaseSerializer.Meta.read_only_fields + (
            "order_total",
            "additional_discount",
            "grand_total",
        )


class AdminOrderDetailSerializer(OrderBaseSerializer):
    order_items = OrderItemListSerializer(read_only=True, many=True)

    class Meta(OrderBaseSerializer.Meta):
        fields = OrderBaseSerializer.Meta.fields + (
            "order_items",
            "complete",
            "order_total",
            "additional_discount",
            "grand_total",
            "created_at",
            "updated_at",
        )
        read_only_fields = OrderBaseSerializer.Meta.read_only_fields + (
            "order_total",
            "grand_total",
            "created_at",
            "updated_at",
        )

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        instance.grand_total = instance.order_total - validated_data.get(
            "additional_discount", 0.00
        )
        instance.updated_by_id = user.id
        return super().update(instance, validated_data)
