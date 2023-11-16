# """
# This is index settings for elastic search.
# To declare index in separate file we need to config index
# """
# from django_elasticsearch_dsl import Index
# from django.conf import settings


# def get_index(document_name="main"):
#     # create an index and register the doc types
#     # index_name = "{}_{}".format(settings.ES_INDEX, document_name)
#     index = Index(document_name)
#     index.settings(**settings.ES_INDEX_SETTINGS)
#     return index
