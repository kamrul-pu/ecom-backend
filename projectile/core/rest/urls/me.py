"""User Urls"""

from django.urls import path

from core.rest.views.me import (
    UserProfile,
)

urlpatterns = [
    path("", UserProfile.as_view(), name="user-profile"),
]
