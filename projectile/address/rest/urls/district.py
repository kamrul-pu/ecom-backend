"""Address app district urls mappings."""
from django.urls import path
from address.rest.views.district import DistrictList, DistrictDetail


urlpatterns = [
    path("", DistrictList.as_view(), name="district-list"),
    path("/<uuid:uid>", DistrictDetail.as_view(), name="district-detail"),
]
