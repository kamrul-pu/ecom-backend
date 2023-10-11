"""Product related base urls."""
from django.urls import path, include


urlpatterns = [
    path(
        "/manufacturer", include("product.rest.urls.manufacturer"), name="manufacturer"
    ),
    path("/brands", include("product.rest.urls.brand"), name="brand"),
    path("/categories", include("product.rest.urls.category"), name="category"),
]
