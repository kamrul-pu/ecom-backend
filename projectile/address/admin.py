from django.contrib import admin

from address.models import (
    Address,
    District,
    Upazila,
    Division,
)


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = [
        "id",
        "uid",
        "label",
        "district",
        "country",
    ]
    readonly_fields = ("uid",)


admin.site.register(Address, AddressAdmin)


class DistrictAdmin(admin.ModelAdmin):
    model = District
    list_display = (
        "id",
        "uid",
        "name",
    )


admin.site.register(District, DistrictAdmin)


class DivisionAdmin(admin.ModelAdmin):
    model = Division
    list_display = (
        "id",
        "uid",
        "name",
    )


admin.site.register(Division, DivisionAdmin)


class UpazilaAdmin(admin.ModelAdmin):
    model = District
    list_display = (
        "id",
        "uid",
        "name",
    )


admin.site.register(Upazila, UpazilaAdmin)
