from django.urls import reverse


def get_token_url():
    return reverse("token_obtain_pair")


def get_user_list_create_url():
    return reverse("user_list-create")


def get_user_detail_update_url(uid: str):
    return reverse("user-details", args=[uid])
