"""Serializers for Upazilla model."""

from rest_framework import serializers

from address.models import Upazila


class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upazila
        fields = (
            "id",
            "uid",
            "name",
            "bengali_name",
            "latitude",
            "longitude",
        )
        read_only_fields = (
            "id",
            "uid",
        )


class UpazilaListSerializer(UpazilaSerializer):
    class Meta(UpazilaSerializer.Meta):
        fields = UpazilaSerializer.Meta.fields + (
            "district",
            "division",
        )

        read_only_fields = UpazilaSerializer.Meta.read_only_fields + ()
