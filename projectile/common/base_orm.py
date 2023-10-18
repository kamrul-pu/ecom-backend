from product.models import Brand, Manufacturer, Category
from address.models import Division, District, Upazila


def create_brand(name="Test Brand"):
    brand, created = Brand.objects.get_or_create(name=name)
    return brand


def create_category(name="Test Category"):
    category, created = Category.objects.get_or_create(name=name)
    return category


def create_manufacturer(name="Test Manufacturer"):
    manufacturer, created = Manufacturer.objects.get_or_create(name=name)
    return manufacturer


def create_division(name="Test Division"):
    division, created = Division.objects.get_or_create(name=name)
    return division


def create_district(name="Test District"):
    district, created = District.objects.get_or_create(
        name=name, division=create_division()
    )
    return district


def create_upazila(name="Test Upazila"):
    upazila, created = Upazila.objects.get_or_create(
        name=name, division=create_division(), district=create_district()
    )
    return upazila
