from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size_query_param = "page_size"


class ListPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        from rest_framework.response import Response
        from rest_framework import status

        return Response(
            {
                "code": status.HTTP_200_OK,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "results": data,
            }
        )
