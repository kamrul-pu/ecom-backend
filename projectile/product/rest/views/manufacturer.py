"""Views for Manufacturer Model"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.permissions import (
    IsAdminUser,
    IsSuperAdmin,
    IsAuthenticatedOrReadOnly,
)

from product.models import Manufacturer

from product.rest.serializers.manufacturer import (
    ManufacturerListSerializer,
    ManufacturerDetailSerializer,
)


class ManufacturerList(ListCreateAPIView):
    serializer_class = ManufacturerListSerializer
    queryset = Manufacturer().get_all_actives()

    permission_classes = (IsAdminUser | IsSuperAdmin | IsAuthenticatedOrReadOnly,)


class ManufacturerDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ManufacturerDetailSerializer
    queryset = Manufacturer().get_all_actives()
    lookup_field = "uid"
    permission_classes = (IsSuperAdmin | IsAdminUser,)
