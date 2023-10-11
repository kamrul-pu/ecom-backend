"""Serializers for Category model."""

from rest_framework import serializers

from product.models import Category


class CategoryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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


class CategoryListSerializer(CategoryBaseSerializer):
    class Meta(CategoryBaseSerializer.Meta):
        fields = CategoryBaseSerializer.Meta.fields + (
            "description",
            "image",
        )
        read_only_fields = CategoryBaseSerializer.Meta.read_only_fields + ()

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["entry_by_id"] = user.id
        return super().create(validated_data)


class CategoryDetailSerializer(CategoryBaseSerializer):
    class Meta(CategoryBaseSerializer.Meta):
        fields = CategoryBaseSerializer.Meta.fields + (
            "description",
            "image",
            "entry_by",
            "updated_by",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = CategoryBaseSerializer.Meta.read_only_fields + (
            "entry_by",
            "updated_by",
            "created_at",
            "updated_at",
        )

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        validated_data["updated_by_id"] = user.id
        return super().update(instance, validated_data)
