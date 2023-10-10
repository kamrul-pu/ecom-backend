from rest_framework import serializers

from product.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "uid",
            "slug",
            "name",
            "description",
            "entry_by",
            "updated_by",
            "image",
            "status",
        ]
        read_only_fields = (
            "id",
            "uid",
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "uid",
            "slug",
            "name",
            "description",
            "entry_by",
            "updated_by",
            "slug",
            "image",
            "status",
        ]
        read_only_fields = (
            "id",
            "uid",
            "slug",
            "status",
        )
