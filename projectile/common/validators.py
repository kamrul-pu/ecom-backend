import os
import json
import re
from rest_framework.exceptions import ValidationError

from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


def validate_phone_number_with_and_without_country_code(phone):
    error = "INCORRECT_MOBILE_NUMBER"
    file_path = os.path.join(
        settings.REPO_DIR,
        "projectile/tmp/country-code.json",
    )

    # country_codes = get_json_data_from_file('tmp/country-code.json')
    with open(file_path, "r", encoding="utf-8") as f:
        country_codes = json.load(f)

    # Check if the phone number matches the format with a country code or without
    if not (re.match(r"^\+\d{3}[0-9]{10}$", phone) or re.match(r"^0[0-9]{10}$", phone)):
        raise ValidationError(error)

    # If the phone number starts with '+', extract the country code
    if phone[0] == "+":
        match = re.match(r"^(\+\d{3})[0-9]{10}$", phone)
        if not match:
            raise ValidationError(error)
        country_code = match.group(1)

        # get the phone number without the country code and adding '0' at the beginning
        phone = "0" + phone[len(country_code) :]

        # Check if the country code exists in the dictionary
        if country_code not in country_codes:
            raise ValidationError("Invalid country code")

    # Check if the phone number is already registered
    if User().get_all_actives().filter(phone_number=phone).exists():
        raise ValidationError("This phone number is already registered.")

    return phone
