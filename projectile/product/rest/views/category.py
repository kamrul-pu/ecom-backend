"""Views for Categorys"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from core.permissions import (
    IsAdminUser,
    IsSuperAdmin,
    IsAuthenticatedOrReadOnly,
    IsAdminUserOrReadOnly,
)

from product.models import Category

from product.rest.serializers.category import (
    CategoryListSerializer,
    CategoryDetailSerializer,
)


class CategoryList(ListCreateAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category().get_all_actives()

    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == "GET":
            return [
                AllowAny(),
            ]
        else:
            return [
                IsSuperAdmin() or IsAdminUser(),
            ]


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category().get_all_actives()
    lookup_field = "uid"
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == "GET":
            return [
                AllowAny(),
            ]
        else:
            return [
                IsSuperAdmin() or IsAdminUser(),
            ]
