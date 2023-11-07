from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from product.documents import ProductDocument
from product.rest.serializers.product import ProductListSerializer


class ProductSearchList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductListSerializer

    def get_queryset(self):
        query_value = self.request.query_params.get("keyword", None)
        search = ProductDocument().search()
        if query_value:
            search = search.query(
                "match",
                name=query_value,
            )
        response = search.execute()

        return response
