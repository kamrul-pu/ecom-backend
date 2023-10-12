"""Product Related Urls Mapping"""
from django.urls import path

from product.rest.views.product import (
    ProductList,
    ProductDetail,
)

urlpatterns = [
    path("", ProductList.as_view(), name="product-list-create"),
    path("/<uuid:uid>", ProductDetail.as_view(), name="product-details"),
]
