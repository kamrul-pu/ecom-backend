from product.models import Brand, Manufacturer, Category


def create_brand(name="Test Brand"):
    brand, created = Brand.objects.get_or_create(name=name)
    return brand


def create_category(name="Test Category"):
    category, created = Category.objects.get_or_create(name=name)
    return category


def create_manufacturer(name="Test Manufacturer"):
    manufacturer, created = Manufacturer.objects.get_or_create(name=name)
    return manufacturer
