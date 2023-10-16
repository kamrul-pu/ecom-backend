"""Views for Product Model"""
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from core.permissions import (
    IsAdminUser,
    IsSuperAdmin,
)

from product.models import Product
from product.rest.serializers.product import (
    ProductListSerializer,
    ProductDetailSerializer,
    ProductPostSerializer
)


class ProductList(ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product().get_all_actives()

    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    filterset_fields = (
        "category",
        "brand",
        "manufacturer",
        "name",
    )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductListSerializer
        else:
            return ProductPostSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [
                AllowAny(),
            ]
        else:
            return [
                IsSuperAdmin() or IsAdminUser(),
            ]

    def get_queryset(self):
        queryset = self.queryset.filter().annotate(
            brand_name=F("brand__name"),
            category_name=F("category__name"),
            manufacturer_name=F("manufacturer__name"),
        )

        return queryset


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product().get_all_actives()
    lookup_field = "uid"

    def get_queryset(self):
        queryset = self.queryset.filter().annotate(
            brand_name=F("brand__name"),
            category_name=F("category__name"),
            manufacturer_name=F("manufacturer__name"),
        )

        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductListSerializer
        else:
            return ProductDetailSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [
                AllowAny(),
            ]
        else:
            return [
                IsSuperAdmin() or IsAdminUser(),
            ]
