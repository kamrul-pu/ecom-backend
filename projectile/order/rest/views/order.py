"""Views for order."""
from django_filters import rest_framework as filters

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from core.permissions import IsAdminUser, IsSuperAdmin
from order.models import Order
from order.choices import OrderType
from order.rest.serializers.order import (
    AdminOrderListSerializer,
    AdminOrderDetailSerializer,
)


class AdminOrderList(ListAPIView):
    serializer_class = AdminOrderListSerializer
    permission_classes = (IsAdminUser | IsSuperAdmin,)
    queryset = Order().get_all_actives()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        "customer",
        "delivery_date",
        "order_type",
        "order_status",
        "payment_method",
        "payment_status",
    )


class AdminOrderDetail(RetrieveUpdateAPIView):
    permission_classes = (IsAdminUser | IsSuperAdmin,)
    serializer_class = AdminOrderDetailSerializer
    queryset = Order().get_all_actives()
    lookup_field = "uid"
