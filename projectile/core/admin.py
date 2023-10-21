"""
Django admin customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User, PasswordReset


class UserAdmin(BaseUserAdmin):
    """Defines the admin pages for users."""

    ordering = ["-id"]
    list_display = ["id", "uid", "phone_number", "email", "full_name", "kind", "status"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "password",
                    "full_name",
                    "image",
                    "kind",
                    "status",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "full_name",
                    "image",
                    "kind",
                    "status",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)


class PasswordResetAdmin(admin.ModelAdmin):
    model = PasswordReset
    list_display = [
        "id",
        "uid",
        "user",
        "phone",
        "reset_status",
        "type"
    ]
    readonly_fields = ("uid",)


admin.site.register(PasswordReset, PasswordResetAdmin)
