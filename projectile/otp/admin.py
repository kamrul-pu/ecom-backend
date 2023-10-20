from django.contrib import admin

from otp.models import OTP


# Register your models here.
@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    model = OTP
    list_display = [
        "id",
        "uid",
        "otp",
        "type",
        "is_used",
        "user",
    ]
    readonly_fields = ("uid",)
