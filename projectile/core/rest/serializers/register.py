from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from common.validators import validate_phone_number_with_and_without_country_code

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        min_length=11, max_length=20,
        validators=[
            validate_phone_number_with_and_without_country_code,
        ],
        error_messages={"phone_number": "This phone number is already registered."}
    )

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
            "phone_number",
            "full_name",
            "email",
            "gender",
            "image",
            "password",
            "confirm_password",
        ]
        read_only_fields = (
            "id",
            "uid",
            "slug",
        )

    def validate_password(self, value):
        confirm_password = self.initial_data.get("confirm_password", "")
        if confirm_password != value:
            raise serializers.ValidationError(
                {"detail": "Confirm password do not matched with password!"}
            )
        return value

    def create(self, validated_data):
        with transaction.atomic():
            password = validated_data.pop("password", None)
            validated_data.pop("confirm_password", None)

            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()

            return user
