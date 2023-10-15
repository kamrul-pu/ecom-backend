"""BASE url mappings for address app"""

from django.urls import path, include


urlpatterns = [
    path("", include("address.rest.urls.address"), name="addresses"),
    path("/divisions", include("address.rest.urls.division"), name="divisions"),
    path("/districts", include("address.rest.urls.district"), name="distrcits"),
    path("/upazilas", include("address.rest.urls.upazila"), name="upazilas"),
]
