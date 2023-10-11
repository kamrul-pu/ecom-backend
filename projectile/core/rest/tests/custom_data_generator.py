import random
import string
import tempfile
import os

from faker.providers import BaseProvider
from PIL import Image, ImageDraw


class CustomDataGenerator(BaseProvider):
    def generate_phone_number(self):
        return (
            "0"
            + str(self.random_element(["17", "18", "19", "16", "15", "13", "14"]))
            + str(self.random_int(min=10000000, max=99999999))
        )

    def generate_random_password(self):
        return "".join(
            random.choice(string.ascii_letters + string.digits + string.punctuation)
            for _ in range(12)
        )

    def generate_random_email(self):
        username = "".join(random.choices(string.ascii_letters, k=10))
        domain = "".join(random.choices(string.ascii_lowercase, k=5))
        extension = random.choice(["com", "net", "org"])
        return f"{username}@{domain}.{extension}"

    def generate_random_image(self, width, height):
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        return image

    def save_image_temporarily(self, image):
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, "random_image.jpg")
        image.save(temp_file_path, format="JPEG")
        return temp_file_path
