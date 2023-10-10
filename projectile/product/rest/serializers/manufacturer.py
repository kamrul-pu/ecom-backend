"""Serializer for manufacturer model."""

from rest_framework import serializers

from product.models import Manufacturer


class ManufacturerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = (
            "id",
            "uid",
            "slug",
            "name",
            "origin",
        )
        read_only_fields = (
            "id",
            "uid",
            "slug",
        )


class ManufacturerListSerializer(ManufacturerBaseSerializer):
    class Meta(ManufacturerBaseSerializer.Meta):
        fields = ManufacturerBaseSerializer.Meta.fields + (
            "description",
            "popularity",
            "logo",
        )
        read_only_fields = ManufacturerBaseSerializer.Meta.read_only_fields + ()

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["entry_by_id"] = user.id
        return super().create(validated_data)


class ManufacturerDetailSerializer(ManufacturerBaseSerializer):
    class Meta(ManufacturerBaseSerializer.Meta):
        fields = ManufacturerBaseSerializer.Meta.fields + (
            "description",
            "popularity",
            "logo",
            "entry_by",
            "updated_by",
            "created_at",
            "updated_at",
        )
        read_only_fields = ManufacturerBaseSerializer.Meta.read_only_fields + (
            "created_at",
            "updated_at",
            "entry_by",
            "updated_by",
        )

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        validated_data["updated_by_id"] = user.id
        return super().update(instance, validated_data)
