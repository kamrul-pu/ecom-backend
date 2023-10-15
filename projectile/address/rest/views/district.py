"""Views for address app"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from address.models import District
from address.rest.serializers.district import DistrictListSerializer

from core.permissions import (
    IsSuperAdmin,
    IsAdminUser,
)


class DistrictList(ListCreateAPIView):
    serializer_class = DistrictListSerializer
    queryset = District().get_all_actives().order_by("name")
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

    def get_queryset(self):
        division = self.request.query_params.get("division", None)
        queryset = self.queryset
        if division:
            queryset = queryset.filter(
                division_id=division,
            )
        return queryset


class DistrictDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = DistrictListSerializer
    queryset = District().get_all_actives().order_by("name")
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
