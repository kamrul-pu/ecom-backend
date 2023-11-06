from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework.exceptions import APIException

from common.serializers import BaseSerializer
from common.validators import validate_phone_number_with_and_without_country_code
from core.choices import UserKind
from core.utils import is_valid_bangladeshi_number

User = get_user_model()


class UserMeta(BaseSerializer.Meta):
    model = User
    fields = BaseSerializer.Meta.fields + (
        "slug",
        "full_name",
        "phone_number",
        "email",
        "gender",
    )
    read_only_fields = BaseSerializer.Meta.read_only_fields + ("slug",)


class UserModelSerializer:
    class List(BaseSerializer):
        class Meta(UserMeta):
            fields = UserMeta.fields + ()

    class Post(BaseSerializer):
        password = serializers.CharField(
            write_only=True,
            required=True,
        )
        confirm_password = serializers.CharField(
            write_only=True,
            required=True,
        )

        class Meta(UserMeta):
            fields = UserMeta.fields + (
                "password",
                "confirm_password",
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

    class Details(BaseSerializer):
        class Meta(UserMeta):
            fields = UserMeta.fields + (
                "image",
                "kind",
                "status",
            )

    class UserUpdate(BaseSerializer):
        class Meta(UserMeta):
            fields = UserMeta.fields + (
                "image",
                "kind",
                "status",
            )
            read_only_fields = UserMeta.read_only_fields + (
                "kind",
                "status",
            )

        def validate_phone_number(self, value):
            if value and not is_valid_bangladeshi_number(value):
                raise APIException(
                    {"detail": "Invalid, This is not a Bangladeshi Phone Number."}
                )
            return value

    class UserRegistrationSerializer(BaseSerializer):
        phone_number = serializers.CharField(
            min_length=11,
            max_length=20,
            validators=[
                validate_phone_number_with_and_without_country_code,
            ],
            error_messages={"phone_number": "This phone number is already registered."},
        )

        password = serializers.CharField(
            write_only=True,
            required=True,
        )
        confirm_password = serializers.CharField(
            write_only=True,
            required=True,
        )

        class Meta(UserMeta):
            fields = UserMeta.fields + (
                "image",
                "password",
                "confirm_password",
            )
            read_only_fields = UserMeta.read_only_fields + ()

        def validate_password(self, value):
            confirm_password = self.initial_data.get("confirm_password", "")
            if confirm_password != value:
                raise serializers.ValidationError(
                    {"detail": "Confirm password do not matched with password!"}
                )
            return value

        def create(self, validated_data):
            password = validated_data.pop("password", None)
            validated_data.pop("confirm_password", None)

            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.kind = UserKind.CUSTOMER
            user.save()

            return user
