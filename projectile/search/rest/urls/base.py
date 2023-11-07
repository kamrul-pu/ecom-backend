"""Base url mappings for search."""

from django.urls import path, include

urlpatterns = [
    path("/products", include("search.rest.urls.products"), name="products"),
]
