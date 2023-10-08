"""Utils functions for core app."""

import re


# Media File Prefixes
def get_user_media_path_prefix(instance, filename):
    return f"users/{instance.slug}/{filename}"


def is_valid_bangladeshi_number(phone_number: str):
    # Regular expression for Bangladeshi phone numbers with optional '+88'
    pattern = re.compile(r"^(\+88)?01[3-9]\d{8}$")

    # Check if the phone number matches the pattern
    return bool(pattern.match(phone_number))
