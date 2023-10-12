"""Models for handling Order Cart Related Data."""

from django.db import models

from autoslug import AutoSlugField

from common.models import BaseModelWithUID

from order.choices import (
    OrderStatus,
    OrderType,
    PaidBy,
    PaymentMethod,
    PaymentStatus,
)


class Order(BaseModelWithUID):
    customer = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="customer_orders",
    )
    complete = models.BooleanField(
        default=False,
    )
    delivery_date = models.DateField(
        blank=True,
        null=True,
    )
    order_type = models.CharField(
        max_length=30,
        choices=OrderType.choices,
        default=OrderType.DEFAULT,
    )
    payment_method = models.CharField(
        max_length=30,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CASH_ON_DELIVERY,
    )
    payment_status = models.CharField(
        max_length=30,
        choices=PaymentStatus.choices,
        default=PaymentStatus.DEFAULT,
    )
    order_status = models.CharField(
        max_length=30,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    additional_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )

    def __str__(self) -> str:
        return f"{self.id} - {self.customer} - {self.order_status}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(BaseModelWithUID):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        related_name="product_order_items",
    )
    product_name = models.CharField(
        max_length=255,
        blank=True,
    )
    quantity = models.PositiveIntegerField(
        default=0,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )

    def __str__(self) -> str:
        return f"id: {self.id} - order: {self.order}"

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"


class OrderPayment(BaseModelWithUID):
    customer = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        related_name="customer_payments",
        blank=True,
        null=True,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        related_name="order_payments",
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    paid_by = models.CharField(
        max_length=30,
        choices=PaidBy.choices,
        default=PaidBy.CASH,
    )

    def __str__(self) -> str:
        return f"{self.id} - {self.customer} - {self.amount}"
