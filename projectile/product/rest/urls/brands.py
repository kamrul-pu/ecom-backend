from django.urls import path
from product.rest.views.brands import BrandList, BrandDetail

urlpatterns = [
    path("", BrandList.as_view(), name="brand-list-create"),
    path("/<uuid:uid>", BrandDetail.as_view(), name="brand-details"),
]
