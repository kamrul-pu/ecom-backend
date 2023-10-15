from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework.exceptions import APIException

from core.utils import is_valid_bangladeshi_number

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "uid",
            "slug",
            "full_name",
            "phone_number",
            "email",
            "gender",
            "image",
            "kind",
            "status",
            "password",
            "confirm_password",
        ]
        read_only_fields = (
            "id",
            "uid",
            "slug",
        )

    def validate_phone_number(self, value):
        if value and not is_valid_bangladeshi_number(value):
            raise APIException({"Phone number is invalid"})
        return value

    def validate_password(self, value):
        confirm_password = self.initial_data.get("confirm_password", "")
        if confirm_password != value:
            raise APIException(
                {"detail": "Confirm password do not matched with password!"}
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        validated_data.pop("confirm_password", None)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "uid",
            "slug",
            "full_name",
            "email",
            "phone_number",
            "image",
            "gender",
            "image",
            "kind",
            "status",
        )
        read_only_fields = (
            "id",
            "uid",
            "slug",
            "kind",
            "status",
        )

    def validate_phone_number(self, value):
        if value and not is_valid_bangladeshi_number(value):
            raise APIException(
                {"detail": "Invalid, This is not a Bangladeshi Phone Number."}
            )
        return value
