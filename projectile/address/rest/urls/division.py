"""Address app divisions urls mappings."""
from django.urls import path
from address.rest.views.division import DivisionList, DivisionDetail


urlpatterns = [
    path("", DivisionList.as_view(), name="division-list"),
    path("/<uuid:uid>", DivisionDetail.as_view(), name="division-detail"),
]
