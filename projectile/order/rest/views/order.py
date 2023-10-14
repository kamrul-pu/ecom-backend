"""Views for order."""
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


class AdminOrderDetail(RetrieveUpdateAPIView):
    permission_classes = (IsAdminUser | IsSuperAdmin,)
    serializer_class = AdminOrderDetailSerializer
    queryset = Order().get_all_actives()
    lookup_field = "uid"
