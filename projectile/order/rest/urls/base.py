"""Base URL mapping for order app."""

from django.urls import include, path

urlpatterns = [
    path("/cart", include("order.rest.urls.cart"), name="customer-cart"),
]
