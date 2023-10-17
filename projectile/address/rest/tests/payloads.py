from faker import Factory

from common.base_orm import create_district, create_division, create_upazila
from core.rest.tests.custom_data_generator import CustomDataGenerator

faker = Factory.create()
custom_generator = CustomDataGenerator(faker)


def address_create_payload():
    return {
        "label": faker.word(),
        "house_street": faker.street_address(),
        "division": create_division().id,
        "district": create_district().id,
        "upazila": create_upazila().id,
        "latitude": faker.latitude(),
        "longitude": faker.longitude(),
    }


def address_update_payload():
    return {
        "label": faker.word(),
        "house_street": faker.street_address(),
        "upazila": create_upazila(name="Update Upazila").id,
    }


def division_create_payload():
    return {
        "name": faker.word(),
        "bengali_name": faker.word(),
        "latitude": faker.latitude(),
        "longitude": faker.longitude(),
    }


def division_update_payload():
    return {
        "name": faker.word(),
        "latitude": faker.latitude(),
        "longitude": faker.longitude(),
    }


def district_create_payload():
    return {
        "name": faker.word(),
        "bengali_name": faker.word(),
        "latitude": faker.latitude(),
        "longitude": faker.longitude(),
        "division": create_division().id,
    }


def district_update_payload():
    return {
        "name": faker.word(),
        "latitude": faker.latitude(),
        "division": create_division(name="Update Division").id,
    }
