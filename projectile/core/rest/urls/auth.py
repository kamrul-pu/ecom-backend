from django.urls import path
from core.rest.views.auth import UserRegistration, UserPasswordReset

urlpatterns = [
    path("/register", UserRegistration.as_view(), name="user-register"),
    path("/password-reset", UserPasswordReset.as_view(), name="user-password-reset"),
]
