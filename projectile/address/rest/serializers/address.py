"""Serializers for Address App."""

from rest_framework import serializers

from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "uid",
            "status",
        )
        read_only_fields = ("id", "uid", "status")


class AddressListSerializer(AddressSerializer):
    class Meta(AddressSerializer.Meta):
        fields = AddressSerializer.Meta.fields + (
            "label",
            "house_street",
            "division",
            "district",
            "upazila",
            "latitude",
            "longitude",
        )
        read_only_fields = AddressSerializer.Meta.read_only_fields + ()

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["user_id"] = user.id

        return super().create(validated_data)
