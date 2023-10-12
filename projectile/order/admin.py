"""Include models in the Admin Panel."""

from django.contrib import admin

from order.models import (
    Order,
    OrderItem,
    OrderPayment,
)


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order
        list_display = (
            "id",
            "uid",
            "order_type",
            "order_status",
            "payment_status",
            "grand_total",
            "status",
        )


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    class Meta:
        model = OrderItem
        list_display = (
            "id",
            "uid",
            "order",
            "product",
            "quantity",
            "price",
            "total",
            "status",
        )


admin.site.register(OrderItem, OrderItemAdmin)


class OrderPaymentAdmin(admin.ModelAdmin):
    class Meta:
        model = OrderPayment
        list_display = (
            "id",
            "uid",
            "customer",
            "order",
            "amount",
            "status",
        )


admin.site.register(OrderPayment, OrderPaymentAdmin)
