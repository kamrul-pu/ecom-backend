"""Serializers for Address App division model."""

from rest_framework import serializers

from address.models import (
    Division,
    District,
)


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = (
            "id",
            "uid",
            "name",
        )
        read_only_fields = (
            "id",
            "uid",
        )


class DivisionListSerializer(DivisionSerializer):
    class Meta(DivisionSerializer.Meta):
        fields = DivisionSerializer.Meta.fields + ()
        read_only_fields = DivisionSerializer.Meta.read_only_fields + ()


class DivisionPostSerializer(DivisionSerializer):
    class Meta(DivisionSerializer.Meta):
        fields = DivisionSerializer.Meta.fields + (
            "bengali_name",
            "latitude",
            "longitude",
        )
        read_only_fields = DivisionSerializer.Meta.read_only_fields + ()

