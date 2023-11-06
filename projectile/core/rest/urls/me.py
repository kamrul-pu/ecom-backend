"""User Urls"""

from django.urls import path

from core.rest.views.me import (
    UserProfile,
    UserRegistration,
    UserPasswordReset,
)

urlpatterns = [
    path("", UserProfile.as_view(), name="user-profile"),
    path("/register", UserRegistration.as_view(), name="user-register"),
    path("/password-reset", UserPasswordReset.as_view(), name="user-password-reset"),
]
