from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from product.models import Brand
from product.rest.serializers.brands import (
    BrandListSerializer,
    BrandDetailSerializer,
)


class BrandList(ListCreateAPIView):
    serializer_class = BrandListSerializer
    permission_classes = (IsAdminUser,)
    queryset = Brand().get_all_actives()


class BrandDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BrandDetailSerializer
    permission_classes = (IsAdminUser,)
    queryset = Brand().get_all_actives()
    lookup_field = "uid"
