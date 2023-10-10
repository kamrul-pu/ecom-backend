"""Manufacturer Related Urls Mapping"""
from django.urls import path

from product.rest.views.manufacturer import (
    ManufacturerList,
    ManufacturerDetail,
)

urlpatterns = [
    path("", ManufacturerList.as_view(), name="manufacturer-list-create"),
    path("/<uuid:uid>", ManufacturerDetail.as_view(), name="manufacturer-detail"),
]
