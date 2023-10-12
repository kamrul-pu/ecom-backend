"""Views for Product Model"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.permissions import (
    IsAdminUser,
    IsSuperAdmin,
    IsAuthenticatedOrReadOnly,
)

from product.models import Product

from product.rest.serializers.product import (
    ProductListSerializer,
    ProductDetailSerializer,
)


class ProductList(ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product().get_all_actives()

    permission_classes = (IsAdminUser | IsSuperAdmin | IsAuthenticatedOrReadOnly,)


class ProductDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product().get_all_actives()
    lookup_field = "uid"
    permission_classes = (IsSuperAdmin | IsAdminUser,)
