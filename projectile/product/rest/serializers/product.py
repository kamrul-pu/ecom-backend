"""Serializer for Product model."""

from rest_framework import serializers

from product.models import Product


class ProductBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "uid",
            "slug",
            "name",
            "buying_price",
            "mrp",
            "discount",
            "discounted_price",
            "stock",
            "is_published",
            "is_salesable",
            "image",
            "rating",
        )
        read_only_fields = (
            "id",
            "uid",
            "slug",
        )


class ProductListSerializer(ProductBaseSerializer):
    brand_name = serializers.CharField(read_only=True)
    category_name = serializers.CharField(read_only=True)
    manufacturer_name = serializers.CharField(read_only=True)

    class Meta(ProductBaseSerializer.Meta):
        fields = ProductBaseSerializer.Meta.fields + (
            "brand_name",
            "category_name",
            "manufacturer_name",
        )
        read_only_fields = ProductBaseSerializer.Meta.read_only_fields + ()


class ProductPostSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        fields = ProductBaseSerializer.Meta.fields + (
            "brand",
            "category",
            "manufacturer",
        )
        read_only_fields = ProductBaseSerializer.Meta.read_only_fields + ()

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["entry_by_id"] = user.id
        validated_data["discounted_price"] = validated_data.get(
            "mrp", 0.0
        ) - validated_data.get("discount", 0.0)
        return super().create(validated_data)


class ProductDetailSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        fields = ProductBaseSerializer.Meta.fields + (
            "brand",
            "category",
            "manufacturer",
            "entry_by",
            "updated_by",
            "created_at",
            "updated_at",
        )
        read_only_fields = ProductBaseSerializer.Meta.read_only_fields + (
            "created_at",
            "updated_at",
            "entry_by",
            "updated_by",
        )

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        validated_data["updated_by_id"] = user.id
        return super().update(instance, validated_data)
