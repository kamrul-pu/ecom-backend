from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserPasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset OTP
    """
    phone_number = serializers.CharField(
        required=True,
        min_length=11,
        max_length=20
    )

    new_password = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        write_only=True
    )
    confirm_password = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        write_only=True
    )
    otp = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        write_only=True
    )