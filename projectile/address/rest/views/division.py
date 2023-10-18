"""Views for address app"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from address.models import Division
from address.rest.serializers.division import (
    DivisionListSerializer,
    DivisionPostSerializer,
)

from core.permissions import (
    IsSuperAdmin,
    IsAdminUser,
)


class DivisionList(ListCreateAPIView):
    queryset = Division().get_all_actives().order_by("name")
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

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DivisionListSerializer
        else:
            return DivisionPostSerializer


class DivisionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Division().get_all_actives().order_by("name")
    lookup_field = "uid"

    def get_permissions(self):
        if self.request.method == "GET":
            return [
                AllowAny(),
            ]
        else:
            return [
                IsSuperAdmin() or IsAdminUser(),
            ]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DivisionListSerializer
        else:
            return DivisionPostSerializer
