"""Address app address urls mappings."""
from django.urls import path
from address.rest.views.address import AddressList, AddressDetail, CustomerAddressUpdate


urlpatterns = [
    path("", AddressList.as_view(), name="address-list"),
    path("/<uuid:uid>", AddressDetail.as_view(), name="address-detail"),
    path("/update", CustomerAddressUpdate.as_view(), name="customer-address-upate"),
]
