"""Views for Customer Cart."""
import json

from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from common.choices import Status

from order.choices import OrderType
from order.models import Order
from order.rest.serializers.order import OrderListSerializer
from order.utils import create_cart, update_cart

from product.models import Product


class CustomerCartList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = (
            Order()
            .get_all_actives()
            .filter(
                customer_id=user.id,
                order_type=OrderType.CART,
            )
        )
        return queryset

    def post(self, request, *args, **kwargs):
        cart_items = request.data.get("cart_items", [])
        user = request.user
        if cart_items:
            cart = create_cart(cart_items, user)
            return Response(
                {
                    "detail": "Cart created successfully",
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "Product is required to create cart"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UpdateCart(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        product_id = request.data.get("product_id", None)
        quantity = request.data.get("quantity", 0)
        user = request.user
        if product_id:
            cart_item = update_cart(
                product_id=product_id, quantity=quantity, user_id=user.id
            )
            return Response(
                {"detail": "Cart Updated Successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "No item to add in the cart"},
            status=status.HTTP_400_BAD_REQUEST,
        )
