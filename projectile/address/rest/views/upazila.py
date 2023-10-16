"""Views for address app upazila models."""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from address.models import Upazila
from address.rest.serializers.upazila import (
    UpazilaListSerializer,
    UpazilaPostSerializer
)

from core.permissions import (
    IsSuperAdmin,
    IsAdminUser,
)


class UpazilaList(ListCreateAPIView):
    queryset = Upazila().get_all_actives().order_by("name")
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
            return UpazilaListSerializer
        else:
            return UpazilaPostSerializer

    def get_queryset(self):
        district = self.request.query_params.get("district", None)
        queryset = self.queryset
        if district:
            queryset = queryset.filter(
                district_id=district,
            )
        return queryset


class UpazilaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Upazila().get_all_actives().order_by("name")
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
            return UpazilaListSerializer
        else:
            return UpazilaPostSerializer
