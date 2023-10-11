from faker import Factory

from django.core.files.uploadedfile import SimpleUploadedFile

from .custom_data_generator import CustomDataGenerator

faker = Factory.create()
custom_generator = CustomDataGenerator(faker)


def superuser_create_payload():
    return {
        "phone_number": custom_generator.generate_phone_number(),
        "password": custom_generator.generate_random_password(),
        "full_name": faker.name(),
    }


def user_create_payload():
    password = custom_generator.generate_random_password()

    random_image = custom_generator.generate_random_image(width=200, height=200)
    temp_image_path = custom_generator.save_image_temporarily(random_image)
    with open(temp_image_path, "rb") as image_file:
        uploaded_image = SimpleUploadedFile(
            name="random_image.jpg",
            content=image_file.read(),
            content_type="image/jpeg",
        )

    return {
        "full_name": faker.name(),
        "phone_number": custom_generator.generate_phone_number(),
        "email": faker.email(),
        "gender": faker.random_element(
            [
                "FEMALE",
                "MALE",
                "UNKNOWN",
                "OTHER",
            ]
        ),
        "image": uploaded_image,
        "kind": faker.random_element(
            [
                "ADMIN",
                "BUYER",
                "CUSTOMER",
                "DELIVERY_MAN",
                "DISTRIBUTOR",
                "SUPER_ADMIN",
                "UNDEFINED",
            ]
        ),
        "status": faker.random_element(["ACTIVE"]),
        "password": password,
        "confirm_password": password,
    }


def user_update_payload():
    return {
        "full_name": faker.name(),
        "phone_number": custom_generator.generate_phone_number(),
        "email": faker.email(),
    }
