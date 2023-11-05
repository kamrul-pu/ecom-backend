# """Document for product related models."""

# from django_elasticsearch_dsl import Document, fields
# from django_elasticsearch_dsl.registries import registry

# from product.models import Category, Product


# @registry.register_document
# class CategoryDocument(Document):
#     class Index:
#         name = "ecom_category"

#     class Django:
#         model = Category
#         fields = [
#             "id",
#             "uid",
#             "name",
#         ]

#     def get_queryset(self):
#         return super().get_queryset(CategoryDocument, self).get_queryset()


# @registry.register_document
# class ProductDocument(Document):
#     id = fields.KeywordField()
#     uid = fields.KeywordField()
#     name = fields.TextField()
#     slug = fields.KeywordField()
#     description = fields.TextField()
#     category = fields.ObjectField(
#         properties={
#             "id": fields.IntegerField(),
#             "uid": fields.TextField(),
#             "name": fields.TextField(),
#         }
#     )
#     mrp = fields.DoubleField()
#     discount = fields.DoubleField()
#     discounted_price = fields.DoubleField()
#     stock = fields.IntegerField()
#     image = fields.TextField()
#     rating = fields.DoubleField()

#     class Index:
#         name = "ecom_products"
#         # settings = {
#         #     "number_of_shards": 1,
#         #     "number_of_replicas": 0,
#         # }

#     class Django:
#         model = Product
#         fields = [
#             "id",
#             "uid",
#             "name",
#             "slug",
#             "description",
#             "category",
#             "mrp",
#             "discount",
#             "discounted_price",
#             "stock",
#             "image",
#             "rating",
#         ]
#         related_models = [Category]

#     def get_queryset(self):
#         return super(ProductDocument, self).get_queryset().select_related("category")
