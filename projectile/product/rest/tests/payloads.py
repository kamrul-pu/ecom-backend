from faker import Factory

from django.core.files.uploadedfile import SimpleUploadedFile

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
