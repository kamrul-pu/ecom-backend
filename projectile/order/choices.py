"""Common Choices for Order APP."""

from django.db.models import TextChoices


class OrderStatus(TextChoices):
    CONFIRMED = "CONFIRMED", "Confirmed"
    CANCELED = "CANCELED", "Canceled"
    DELIVERED = "DELIVERED", "Delivered"
    ON_THE_WAY = "ON_THE_WAY", "On The Way"
    PENDING = "PENDING", "Pending"
    READY_TO_DELIVER = "READY_TO_DELIVER", "Ready To Deliver"
    RETURNED = "RETURNED", "Returned"
    REJECTED = "REJECTED", "Rejected"


class OrderType(TextChoices):
    CART = "CART", "Cart"
    DEFAULT = "DEFAULT", "Default"
    ORDER = "ORDER", "Order"
    PRE_ORDER = "PRE_ORDER", "Pre Order"


class PaymentStatus(TextChoices):
    CANCELED = "CANCELED", "Canceled"
    DEFAULT = "DEFAULT", "Default"
    PAID = "PAID", "Paid"
    PENDING = "PENDING", "Pending"


class PaidBy(TextChoices):
    BANK = "BANK", "BANK"
    BKASH = "BKASH", "Bkash"
    CASH = "CASH", "Cash"
    MOBILE_BANKING = "MOBILE_BANKING", "Mobile Banking"
    NOGOD = "NOGOD", "Nogod"
    ROCKET = "ROCKET", "Rocket"
    OTHER = "OTHER", "Other"


class PaymentMethod(TextChoices):
    ONLINE = "ONLINE", "Online"
    CASH_ON_DELIVERY = "CASH_ON_DELIVERY"
    OTHER = "OTHER", "Other"
