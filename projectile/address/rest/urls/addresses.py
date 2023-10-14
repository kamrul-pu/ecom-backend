"""Product related base urls."""
from django.urls import path
from address.rest.views.addresses import DivisionList, DivisionDetail


urlpatterns = [
    path("/divisions", DivisionList.as_view(), name="division-list"),
    path("/divisions/<uuid:uid>", DivisionDetail.as_view(), name="division-detail")
]
