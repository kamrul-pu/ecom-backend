"""Views for Customer Cart."""

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from common.choices import Status

from order.choices import OrderType
from order.models import Order
from order.rest.serializers.order import OrderListSerializer
from order.utils import update_cart

from product.models import Product


class CustomerCart(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderListSerializer

    def get_object(self):
        user = self.request.user
        cart, created = Order.objects.get_or_create(
            customer_id=user.id,
            order_type=OrderType.CART,
            status=Status.ACTIVE,
        )

        return cart


class UpdateCart(APIView):
    permission_classes = (IsAuthenticated,)

    # def get(self, request, format=None):
    #     cart_items = request.data
    def post(self, request, format=None):
        cart_items = request.data.get("cart_items", [])
        user = request.user
        if cart_items:
            cart, created = Order.objects.get_or_create(
                customer_id=user.id,
                order_type=OrderType.CART,
                status=Status.ACTIVE,
            )
            cart, cart_items = update_cart(cart_items, user)
            print(cart)
            print(cart_items)
            return Response(
                {"detail": "Somethings in the cart", "cart": cart_items},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
        )
