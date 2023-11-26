"""Core models for our app."""

from autoslug import AutoSlugField

from django.contrib.auth.base_user import (
    BaseUserManager,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models

from versatileimagefield.fields import VersatileImageField

from common.models import BaseModelWithUID, NameSlugDescriptionBaseModel

from core.choices import (
    UserKind,
    UserStatus,
    UserGender,
    ResetStatus,
    ResetType,
    OtpType,
)
from core.utils import get_user_media_path_prefix


class UserManager(BaseUserManager):
    """Managers for users."""

    def create_user(self, full_name, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("User must have a phone number")

        user = self.model(
            full_name=full_name, phone_number=phone_number, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, full_name, phone_number, password):
        """Create a new superuser and return superuser"""

        user = self.create_user(
            full_name=full_name, phone_number=phone_number, password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.kind = UserKind.SUPER_ADMIN
        user.status = UserStatus.ACTIVE
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, BaseModelWithUID, PermissionsMixin):
    """Users in the System"""

    phone_number = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
        blank=True,
        null=True,
    )
    nid = models.CharField(
        max_length=20,
        blank=True,
    )
    full_name = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    slug = AutoSlugField(
        populate_from="full_name",
        unique=True,
    )
    gender = models.CharField(
        max_length=20,
        blank=True,
        choices=UserGender.choices,
        default=UserGender.UNKNOWN,
    )
    image = VersatileImageField(
        "Profile_image",
        upload_to=get_user_media_path_prefix,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    kind = models.CharField(
        max_length=20,
        choices=UserKind.choices,
        default=UserKind.UNDEFINED,
    )

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ("full_name",)

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"


# Create your models here.
class OTP(BaseModelWithUID):
    user = models.ForeignKey("core.User", models.DO_NOTHING, related_name="user_otps")
    otp = models.CharField(
        max_length=6,
    )
    type = models.CharField(
        max_length=30,
        choices=OtpType.choices,
        default=OtpType.OTHER,
    )
    is_used = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name_plural = "OTP"

    def __str__(self):
        return f"{self.otp} {self.is_used}"


class PasswordReset(NameSlugDescriptionBaseModel):
    user = models.ForeignKey(
        "core.User",
        models.CASCADE,
        blank=True,
        null=True,
        related_name="password_reset_users",
    )
    phone = models.CharField(max_length=24, db_index=True)
    reset_status = models.CharField(
        max_length=20, choices=ResetStatus.choices, default=ResetStatus.PENDING
    )
    otp = models.ForeignKey(
        "core.OTP",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="password_reset_otps",
    )
    type = models.CharField(
        max_length=20, choices=ResetType.choices, default=ResetType.SELF
    )

    class Meta:
        verbose_name_plural = "PasswordReset"

    def __str__(self):
        return f"{self.phone} - {self.reset_status}"
