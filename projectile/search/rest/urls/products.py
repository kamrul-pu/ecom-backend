"""URL mappings for products."""

from django.urls import path

from search.rest.views.products import ProductSearchList

urlpatterns = [
    path("", ProductSearchList.as_view(), name="product-list"),
]
