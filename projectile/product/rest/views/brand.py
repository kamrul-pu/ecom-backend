"""Views for Brands"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.permissions import (
    IsAdminUser,
    IsSuperAdmin,
    IsAuthenticatedOrReadOnly,
)

from product.models import Brand

from product.rest.serializers.brand import (
    BrandListSerializer,
    BrandDetailSerializer,
)


class BrandList(ListCreateAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand().get_all_actives()

    permission_classes = (IsAdminUser | IsSuperAdmin | IsAuthenticatedOrReadOnly,)


class BrandDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand().get_all_actives()
    lookup_field = "uid"
    permission_classes = (IsSuperAdmin | IsAdminUser,)
