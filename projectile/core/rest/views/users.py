from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAdminUser,
)

from core.models import User
from core.rest.serializers.user import (
    UserListSerializer,
)


class UserList(ListCreateAPIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAdminUser,)
    queryset = User().get_all_actives()


class UserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAdminUser,)
    queryset = User().get_all_actives()
    lookup_field = "uid"
