from django.urls import reverse


def get_category_list_create_url():
    return reverse("category-list-create")


def get_category_detail_update_url(uid: str):
    return reverse("category-details", args=[uid])
