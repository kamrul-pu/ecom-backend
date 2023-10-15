"""Views for address app"""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from address.models import Address
from address.rest.serializers.address import AddressListSerializer

from core.choices import UserKind
from core.permissions import (
    IsSuperAdmin,
    IsAdminUser,
)


class AddressList(ListCreateAPIView):
    serializer_class = AddressListSerializer
    queryset = Address().get_all_actives()
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == "GET":
            return [
                IsSuperAdmin() or IsAdminUser(),
            ]
        else:
            return [
                IsAuthenticated(),
            ]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset
        if user.kind != UserKind.ADMIN or user.kind != UserKind.SUPER_ADMIN:
            queryset = queryset.filter(user_id=user.id)
        return queryset


class AddressDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressListSerializer
    queryset = Address().get_all_actives()
    lookup_field = "uid"
    permission_classes = (IsAdminUser | IsSuperAdmin,)


class CustomerAddressUpdate(RetrieveUpdateAPIView):
    serializer_class = AddressListSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        address = Address.objects.filter(user_id=user.id).order_by("-pk")
        return address.first()
