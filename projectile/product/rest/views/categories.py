from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from product.models import Category
from product.rest.serializers.categories import (
    CategoryListSerializer,
    CategoryDetailSerializer,
)


class CategoryList(ListCreateAPIView):
    serializer_class = CategoryListSerializer
    permission_classes = (IsAdminUser,)
    queryset = Category().get_all_actives()


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = (IsAdminUser,)
    queryset = Category().get_all_actives()
    lookup_field = "uid"
