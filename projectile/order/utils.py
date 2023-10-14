"""Utils functions for order app."""

import decimal

from django.db import transaction
from django.db.models import Q, Sum, Value, F
from django.db.models.functions import Coalesce

from common.choices import Status

from order.choices import OrderType
from order.models import Order, OrderItem

from product.models import Product


def calculate_cart_total(cart):
    calculated_total = (
        OrderItem()
        .get_all_actives()
        .filter(
            order_id=cart.id,
        )
        .aggregate(order_total=Coalesce(Sum("total"), Value(decimal.Decimal("0.00"))))
    )
    order_total = calculated_total.get("order_total", decimal.Decimal("0.00"))
    cart.order_total = order_total
    cart.grand_total = order_total - cart.additional_discount

    cart.save(update_fields=["order_total", "grand_total"])


@transaction.atomic
def update_cart(cart_items, user):
    product_quantity_dict = {
        item["product_id"]: item["quantity"] for item in cart_items
    }
    product_ids = product_quantity_dict.keys()
    # Fetch all relevent product in a single query
    products = Product().get_all_actives().filter(id__in=product_ids)
    print("products", products)
    cart, created = Order.objects.get_or_create(
        customer_id=user.id,
        order_type=OrderType.CART,
        status=Status.ACTIVE,
    )
    items_to_be_removed = []
    cart_items_to_create = []
    cart_items_to_update = []

    # Get all existing cart items
    existing_cart_items = (
        OrderItem()
        .get_all_actives()
        .filter(
            order_id=cart.id,
        )
    )
    existing_cart_items_dict = {
        (cart_item.order_id, cart_item.product_id): cart_item
        for cart_item in existing_cart_items
    }
    print("eeeeeeeeeeeee", existing_cart_items_dict)

    for product in products:
        quantity = product_quantity_dict.get(product.id)
        price = product.discounted_price
        total = quantity * price
        cart_items_data = {
            "order_id": cart.id,
            "product_id": product.id,
            "product_name": product.name,
            "quantity": product_quantity_dict.get(product.id),
            "price": price,
            "total": total,
        }
        existing_cart_item = existing_cart_items_dict.get((cart.id, product.id))
        if existing_cart_item:
            # Update existing cart item if it already exists
            existing_cart_item.quantity = quantity
            existing_cart_item.price = price
            existing_cart_item.total = total
            cart_items_to_update.append(existing_cart_item)
            print("qunatity", quantity)
            if quantity < 1:
                items_to_be_removed.append(existing_cart_item.id)
        else:
            # Append to the list of cart items to create
            cart_items_to_create.append(OrderItem(**cart_items_data))
    # Use bulk_create to insert all new cart items in a single query
    if cart_items_to_create:
        OrderItem.objects.bulk_create(cart_items_to_create)

    # Use bulk_update to update existing cart items in a single query
    if cart_items_to_update:
        OrderItem.objects.bulk_update(
            cart_items_to_update, fields=["quantity", "price", "total"]
        )
    print("items to be remove")
    print(items_to_be_removed)
    # Remove cart items from the cart
    OrderItem.objects.filter(id__in=items_to_be_removed).delete()

    # Calculate Cart total
    calculate_cart_total(cart)

    return {
        "cart": cart,
        "cart_items": cart_items,
    }
