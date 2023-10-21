import random

from twilio.rest import Client
from django.conf import settings


def generate_unique_otp(length=6) -> str:
    otp = "".join(random.choices("0123456789", k=length))

    return otp


def send_sms(phone_number: str, message: str):
    # Twilio client with account SID and auth token

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    if phone_number.startswith('0'):
        phone_number = '+88' + phone_number

    message = client.messages.create(
        to=phone_number,
        from_=settings.TWILIO_PHONE_NUMBER,
        body=message
    )
