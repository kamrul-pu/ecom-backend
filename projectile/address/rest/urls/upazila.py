"""Address app upazila urls mappings."""
from django.urls import path
from address.rest.views.upazila import UpazilaList, UpazilaDetail


urlpatterns = [
    path("", UpazilaList.as_view(), name="upazila-list"),
    path("/<uuid:uid>", UpazilaDetail.as_view(), name="upazila-detail"),
]
