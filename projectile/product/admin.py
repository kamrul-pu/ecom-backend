"""Add Product Related Models in Admin Panel"""

from django.contrib import admin

from product.models import Brand, Category, Manufacturer, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "slug",
        "name",
        "origin",
        "popularity",
        "status",
        "created_at",
    )


admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "slug",
        "name",
        "status",
        "created_at",
    )


admin.site.register(Category, CategoryAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "slug",
        "name",
        "origin",
        "popularity",
        "status",
        "created_at",
    )


admin.site.register(Manufacturer, ManufacturerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "slug",
        "name",
        "status",
        "stock",
        "is_published",
        "mrp",
        "discounted_price",
        "created_at",
    )


admin.site.register(Product, ProductAdmin)
