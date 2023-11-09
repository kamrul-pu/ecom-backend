"""Views for order."""
from django_filters import rest_framework as filters

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsAdminUser, IsSuperAdmin
from common.choices import Status

from order.models import Order
from order.choices import OrderType, OrderStatus
from order.rest.serializers.order import (
    AdminOrderListSerializer,
    AdminOrderDetailSerializer,
    OrderListSerializer,
)


class AdminOrderList(ListAPIView):
    serializer_class = AdminOrderListSerializer
    permission_classes = (IsAdminUser | IsSuperAdmin,)
    queryset = Order().get_all_actives().prefetch_related("order_items")
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


class CustomerOrderList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = (
            Order()
            .get_all_actives()
            .filter(
                customer_id=user.id,
                order_type=OrderType.ORDER,
            )
            .prefetch_related("order_items")
        )

        return queryset

    def post(self, request, *args, **kwargs):
        user = request.user
        cart, created = Order.objects.get_or_create(
            customer_id=user.id,
            order_type=OrderType.CART,
            status=Status.ACTIVE,
        )
        if created or cart.order_items.count() == 0:
            return Response(
                {"detail": "You do not have any item in cart."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart.order_type = OrderType.ORDER
        cart.order_status = OrderStatus.PENDING
        cart.save(update_fields=["order_type", "order_status"])

        return Response(
            {"order": self.serializer_class(cart).data}, status=status.HTTP_201_CREATED
        )
