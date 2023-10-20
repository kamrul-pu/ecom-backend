from django.db import models

from common.models import BaseModelWithUID

from otp.choices import OtpType


# Create your models here.
class OTP(BaseModelWithUID):
    user = models.ForeignKey(
        'core.User',
        models.DO_NOTHING,
        related_name="user_otps"
    )
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
