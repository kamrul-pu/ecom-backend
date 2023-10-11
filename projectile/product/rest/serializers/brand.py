"""Serializers for brand model."""

from rest_framework import serializers

from product.models import Brand


class BrandBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "uid",
            "slug",
            "name",
        )
        read_only_fields = (
            "id",
            "uid",
            "slug",
        )


class BrandListSerializer(BrandBaseSerializer):
    class Meta(BrandBaseSerializer.Meta):
        fields = BrandBaseSerializer.Meta.fields + (
            "origin",
            "popularity",
            "image",
            "description",
        )
        read_only_fields = BrandBaseSerializer.Meta.read_only_fields + ()

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["entry_by_id"] = user.id
        return super().create(validated_data)


class BrandDetailSerializer(BrandBaseSerializer):
    class Meta(BrandBaseSerializer.Meta):
        fields = BrandBaseSerializer.Meta.fields + (
            "origin",
            "popularity",
            "description",
            "image",
            "entry_by",
            "updated_by",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = BrandBaseSerializer.Meta.read_only_fields + (
            "entry_by",
            "updated_by",
            "created_at",
            "updated_at",
        )

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        validated_data["updated_by_id"] = user.id
        return super().update(instance, validated_data)
