"""Views for Product Model"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from core.permissions import (
    IsAdminUser,
    IsSuperAdmin,
    IsAuthenticatedOrReadOnly,
    IsAdminUserOrReadOnly,
)

from product.models import Product

from product.rest.serializers.product import (
    ProductListSerializer,
    ProductDetailSerializer,
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

    permission_classes = (IsAdminUser | IsSuperAdmin | IsAdminUserOrReadOnly,)


class ProductDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product().get_all_actives()
    lookup_field = "uid"
    permission_classes = (IsSuperAdmin | IsAdminUser,)
