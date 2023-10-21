from drf_spectacular.utils import extend_schema

from rest_framework.generics import CreateAPIView

from core.rest.serializers.register import UserRegistrationSerializer


@extend_schema(description="You can register here")
class UserRegistration(CreateAPIView):
    serializer_class = UserRegistrationSerializer
