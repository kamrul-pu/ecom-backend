"""Views for Categorys"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from core.permissions import (
    IsAdminUser,
    IsSuperAdmin,
    IsAuthenticatedOrReadOnly,
)

from product.models import Category

from product.rest.serializers.category import (
    CategoryListSerializer,
    CategoryDetailSerializer,
)


class CategoryList(ListCreateAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category().get_all_actives()

    permission_classes = (IsAdminUser | IsSuperAdmin | IsAuthenticatedOrReadOnly,)


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category().get_all_actives()
    lookup_field = "uid"
    permission_classes = (IsSuperAdmin | IsAdminUser,)
