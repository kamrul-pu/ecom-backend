"""Urls mappings for admin order."""

from django.urls import path

from order.rest.views.order import (
    AdminOrderList,
    AdminOrderDetail,
    CustomerOrderList,
)

urlpatterns = [
    path("", CustomerOrderList.as_view(), name="customer-order-list-create"),
    path("/admin", AdminOrderList.as_view(), name="admin-order"),
    path("/admin/<uuid:uid>", AdminOrderDetail.as_view(), name="admin-order-details"),
]
