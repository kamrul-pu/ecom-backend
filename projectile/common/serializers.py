"""Common Serializers for our app."""

from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer


class BaseSerializer(ModelSerializer):
    class Meta:
        ref_name = ""
        fields = (
            "id",
            "uid",
        )

        read_only_fields = (
            "id",
            "uid",
        )


class LinkSerializer(HyperlinkedModelSerializer):
    class Meta:
        ref_name = ""
        fields = (
            "id",
            "uid",
        )

        read_only_fields = (
            "id",
            "uid",
        )
