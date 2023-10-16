from django.urls import reverse


def get_address_list_create_url():
    return reverse("address-list")


def get_address_detail_update_url(uid: str):
    return reverse("address-detail", args=[uid])


def get_customer_address_update():
    return reverse("customer-address-upate")
