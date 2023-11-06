from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAdminUser,
)

from drf_spectacular.utils import extend_schema


from core.models import User

from core.rest.serializers.user import (
    UserModelSerializer,
)


class UserList(ListCreateAPIView):
    serializer_class = UserModelSerializer.List
    permission_classes = (IsAdminUser,)
    queryset = User().get_all_actives()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserModelSerializer.List
        return UserModelSerializer.Post


class UserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserModelSerializer.Details
    permission_classes = (IsAdminUser,)
    queryset = User().get_all_actives()
    lookup_field = "uid"
