from django.urls import path

from core.rest.views.users import (
    UserList,
    UserDetail,
)


urlpatterns = [
    path("", UserList.as_view(), name="user_list-create"),
    path("/<uuid:uid>", UserDetail.as_view(), name="user-details"),
]
