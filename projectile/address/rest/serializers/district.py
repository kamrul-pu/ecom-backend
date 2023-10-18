"""Serializers for District model."""

from rest_framework import serializers

from address.models import (
    Division,
    District,
)


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = (
            "id",
            "uid",
            "name",
        )
        read_only_fields = (
            "id",
            "uid",
        )


class DistrictListSerializer(DistrictSerializer):
    class Meta(DistrictSerializer.Meta):
        fields = DistrictSerializer.Meta.fields + ()

        read_only_fields = DistrictSerializer.Meta.read_only_fields + ()


class DistrictPostSerializer(DistrictSerializer):
    class Meta(DistrictSerializer.Meta):
        fields = DistrictSerializer.Meta.fields + (
            "bengali_name",
            "latitude",
            "longitude",
            "division",
        )

        read_only_fields = DistrictSerializer.Meta.read_only_fields + ()
