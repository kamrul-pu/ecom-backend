"""Urls mappings for admin order."""

from django.urls import path

from order.rest.views.order import (
    AdminOrderList,
    AdminOrderDetail,
)

urlpatterns = [
    path("", AdminOrderList.as_view(), name="admin-order"),
    path("/<uuid:uid>", AdminOrderDetail.as_view(), name="admin-order-details"),
]