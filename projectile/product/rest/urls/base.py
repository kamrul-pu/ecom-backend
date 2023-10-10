"""Product related base urls."""
from django.urls import path, include


urlpatterns = [
    path(
        "/manufacturer", include("product.rest.urls.manufacturer"), name="manufacturer"
    ),
]
