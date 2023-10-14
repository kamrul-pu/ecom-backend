"""Views for Customer Cart."""

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from order.models import Order

from order.choices import OrderType
from order.rest.serializers.order import OrderListSerializer


class CustomerCart(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderListSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        cart = (
            Order()
            .get_all_actives()
            .filter(
                customer_id=user.id,
                order_type=OrderType.CART,
            )
            .prefetch_related(
                "order_items",
                "order_items__product",
            )
        )
        if cart.exists():
            serializer = self.serializer_class(cart, many=True)
            cart = Order.objects.create(
                customer_id=user.id,
                order_type=OrderType.CART,
            )
            serializer = self.serializer_class(cart)

        return Response({"result": serializer.data}, status=status.HTTP_200_OK)
