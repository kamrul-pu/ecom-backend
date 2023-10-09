"""Our Product Related models should written here."""
from django.db import models

from versatileimagefield.fields import VersatileImageField

from common.models import NameSlugDescriptionBaseModel


class Category(NameSlugDescriptionBaseModel):
    image = VersatileImageField(
        upload_to="category",
        width_field="width",
        height_field="height",
        null=True,
        blank=True,
    )
    width = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    height = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(NameSlugDescriptionBaseModel):
    image = VersatileImageField(
        upload_to="brand",
        width_field="width",
        height_field="height",
        null=True,
        blank=True,
    )
    width = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    height = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    origin = models.CharField(
        max_length=64,
        blank=True,
    )
    popularity = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Manufacturer(NameSlugDescriptionBaseModel):
    origin = models.CharField(
        max_length=64,
        blank=True,
    )
    popularity = models.PositiveIntegerField(
        default=0,
    )
    logo = VersatileImageField(
        upload_to="manufacturer_logo",
        blank=True,
        null=True,
        width_field="width",
        height_field="height",
    )
    width = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    height = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Product Manufacturer"
        verbose_name_plural = "Product Manufacturer"


class Product(NameSlugDescriptionBaseModel):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="brand_products",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="manufacturer_products",
    )
    buying_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )

    mrp = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )

    discounted = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    stock = models.BigIntegerField(
        default=0,
    )
    is_published = models.BooleanField(
        default=True,
    )
    is_salesable = models.BooleanField(
        default=False,
    )
    image = VersatileImageField(
        upload_to="brand",
        width_field="width",
        height_field="height",
        null=True,
        blank=True,
    )
    width = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    height = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
