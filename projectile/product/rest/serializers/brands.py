from rest_framework import serializers

from product.models import Brand


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "uid",
            "slug",
            "name",
            "description",
            "entry_by",
            "updated_by",
            "image",
            "origin",
            "popularity",
            "status",
        ]
        read_only_fields = (
            "id",
            "uid",
        )


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "uid",
            "slug",
            "name",
            "description",
            "entry_by",
            "updated_by",
            "image",
            "origin",
            "popularity",
            "status",
        ]
        read_only_fields = (
            "id",
            "uid",
            "slug",
            "status",
        )
