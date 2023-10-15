import random
from decimal import Decimal
from faker import Factory

from django.core.files.uploadedfile import SimpleUploadedFile

from common.base_orm import create_brand, create_category, create_manufacturer
from core.rest.tests.custom_data_generator import CustomDataGenerator

faker = Factory.create()
custom_generator = CustomDataGenerator(faker)


def category_create_payload():
    random_image = custom_generator.generate_random_image(width=200, height=200)
    temp_image_path = custom_generator.save_image_temporarily(random_image)
    with open(temp_image_path, "rb") as image_file:
        uploaded_image = SimpleUploadedFile(
            name="random_image.jpg",
            content=image_file.read(),
            content_type="image/jpeg",
        )

    return {
        "name": faker.name(),
        "description": faker.text(),
        "image": uploaded_image,
    }


def category_update_payload():
    return {
        "name": faker.name(),
        "description": faker.text(),
    }


def brand_create_payload():
    random_image = custom_generator.generate_random_image(width=200, height=200)
    temp_image_path = custom_generator.save_image_temporarily(random_image)
    with open(temp_image_path, "rb") as image_file:
        uploaded_image = SimpleUploadedFile(
            name="random_image.jpg",
            content=image_file.read(),
            content_type="image/jpeg",
        )

    return {
        "name": faker.name(),
        "origin": faker.text(max_nb_chars=10),
        "popularity": faker.random_element([1, 2, 3, 4, 5]),
        "image": uploaded_image,
        "description": faker.text(),
    }


def brand_update_payload():
    return {
        "name": faker.name(),
        "origin": faker.text(max_nb_chars=10),
        "description": faker.text(),
    }


def manufacturer_create_payload():
    random_image = custom_generator.generate_random_image(width=200, height=200)
    temp_image_path = custom_generator.save_image_temporarily(random_image)
    with open(temp_image_path, "rb") as image_file:
        uploaded_image = SimpleUploadedFile(
            name="random_image.jpg",
            content=image_file.read(),
            content_type="image/jpeg",
        )

    return {
        "name": faker.name(),
        "origin": faker.text(max_nb_chars=10),
        "popularity": faker.random_element([1, 2, 3, 4, 5]),
        "logo": uploaded_image,
        "description": faker.text(),
    }


def manufacturer_update_payload():
    return {
        "name": faker.name(),
        "origin": faker.text(max_nb_chars=10),
        "description": faker.text(),
    }


def product_create_payload():
    random_image = custom_generator.generate_random_image(width=200, height=200)
    temp_image_path = custom_generator.save_image_temporarily(random_image)
    with open(temp_image_path, "rb") as image_file:
        uploaded_image = SimpleUploadedFile(
            name="random_image.jpg",
            content=image_file.read(),
            content_type="image/jpeg",
        )

    return {
        "name": faker.name(),
        "brand": create_brand().id,
        "category": create_category().id,
        "manufacturer": create_manufacturer().id,
        "buying_price": Decimal("%.2f" % random.uniform(1, 1000)),
        "mrp": Decimal("%.2f" % random.uniform(1, 1000)),
        "discount": faker.random_element([0, 5, 10, 15, 20]),
        "stock": faker.random_int(min=0, max=1000),
        "is_published": faker.boolean(chance_of_getting_true=90),
        "is_salesable": faker.boolean(chance_of_getting_true=90),
        "image": uploaded_image,
        "rating": faker.random_element([1, 2, 3, 4, 5]),
    }


def product_update_payload():
    return {
        "name": faker.name(),
        "brand": create_brand(name="Update Brand").id,
        "category": create_category(name="Update Category").id,
    }
