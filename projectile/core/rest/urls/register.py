from django.urls import path
from core.rest.views.register import UserRegistration

urlpatterns = [
    path("/register", UserRegistration.as_view(), name="user-register")
]
