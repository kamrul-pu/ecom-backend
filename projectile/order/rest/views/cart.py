"""Views for Customer Cart."""

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from order.models import Order

from order.choices import OrderType
from order.rest.serializers.order import OrderListSerializer


class CustomerCart(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderListSerializer

    def get_object(self):
        user = self.request.user
        cart, created = Order.objects.get_or_create(
            customer_id=user.id,
            order_type=OrderType.CART,
        )

        return cart
