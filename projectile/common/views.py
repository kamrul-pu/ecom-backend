"""Common views that will be used in another app."""

from django.core.cache import cache

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from common.helpers import pk_extractor
from common.pagintaion import CustomPagination
from common.choices import Status


class ListAPICustomView(ListAPIView):
    available_permission_classes = ()

    def pagination_class(self):
        page_size = self.request.query_params.get("page_size", None)
        if page_size == "showall":
            return None
        else:
            return CustomPagination()

    def get_queryset(self, related_fields=None, only_fields=None):
        if related_fields is None:
            related_fields = []
        if only_fields is None:
            only_fields = []
        # if hasattr(self.get_serializer_class().Meta.model(), "created_at"):
        #     return (
        #         self.get_serializer_class()
        #         .Meta.model()
        #         .get_all_from_organization(
        #             self.request.user.organization_id,
        #             Status.ACTIVE,
        #             "-pk",
        #             related_fields,
        #             only_fields,
        #         )
        #     )
        # else:
        #     return (
        #         self.get_serializer_class()
        #         .Meta.model()
        #         .get_all_from_organization(
        #             self.request.user.organization_id,
        #             Status.ACTIVE,
        #             "pk",
        #             related_fields,
        #             only_fields,
        #         )
        #     )

        return (
            self.get_serializer_class()
            .Meta.model()
            .get_all_actives()
            .select_related(*related_fields)
            .only(*only_fields)
        ).order_by("-pk")


class CreateAPICustomView(CreateAPIView):
    available_permission_classes = ()
    create_data = {}

    def perform_create(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, "entry_by"):
            self.create_data["entry_by_id"] = self.request.user.id

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)


class ListCreateAPICustomView(ListCreateAPIView):
    available_permission_classes = ()
    create_data = {}

    def perform_create(self, serializer, extra_fields):
        try:
            model_class = serializer.Meta.model

        except:
            model_class = self.get_serializer_class().Meta.model

        # if hasattr(model_class, 'organization'):
        #     self.create_data['organization_id'] = self.request.user.organization_id
        if hasattr(model_class, "entry_by"):
            self.create_data["entry_by_id"] = self.request.user.id

        # If request is from reporter server use code to find entry by user
        # entry_by_id = self.request.META.get("HTTP_ENTRY_BY_ID", "")
        # if entry_by_id and checkers.is_integer(entry_by_id):
        #     self.create_data["entry_by_id"] = int(entry_by_id)

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)

    def pagination_class(self):
        page_size = self.request.query_params.get("page_size", None)
        if page_size == "showall":
            return None
        else:
            return CustomPagination()

    def add_extra_fields(self, extra_fields):
        for key in extra_fields:
            self.create_data[key] = extra_fields[key]

    def get_queryset(self, related_fields=None, only_fields=None):
        if related_fields is None:
            related_fields = []
        if only_fields is None:
            only_fields = []
        return (
            self.get_serializer_class()
            .Meta.model()
            .get_all_actives()
            .select_related(*related_fields)
            .only(*only_fields)
        ).order_by("-pk")

    def get_from_cache(self, queryset, request, cache_key=None, response_only=False):
        page = self.paginate_queryset(queryset)
        response = []

        if cache_key is None:
            module = self.get_serializer().__module__
            name = type(self.get_serializer()).__name__
            base_key = "{}.{}".format(module, name).replace(".", "_").lower()
        else:
            base_key = cache_key

        if page is not None:
            # finding every items pk
            objects_pk = pk_extractor(page)

            cache_key_list = [
                "{}_{}".format(base_key, str(item).zfill(12)) for item in objects_pk
            ]

            cached_data = cache.get_many(cache_key_list)
            if len(cached_data) < 20:
                missing_key_data = []

                for index, item in enumerate(cache_key_list):
                    if item not in cached_data:
                        missing_key_data.append(objects_pk[index])

                if missing_key_data:
                    missing_data_queryset = (
                        self.get_serializer()
                        .Meta.model()
                        .get_queryset_for_cache(missing_key_data, request=request)
                    )

                    new_cached_data = {}

                    for each_missing_item in missing_data_queryset:
                        missing_key = "{}_{}".format(
                            base_key, str(each_missing_item.id).zfill(12)
                        )
                        serializer = self.get_serializer_class()(
                            "json",
                            [each_missing_item],
                            many=True,
                        )
                        serializer.is_valid()
                        new_cached_data.update({missing_key: serializer.data[0]})
                        cache.set_many(new_cached_data)

                        cached_data.update(new_cached_data)

            for index, item in enumerate(objects_pk):
                key = "{}_{}".format(base_key, str(item).zfill(12))
                response.append(cached_data[key])

            if response_only:
                return response

        return self.get_paginated_response(response)


class RetrieveUpdateDestroyAPICustomView(RetrieveUpdateDestroyAPIView):
    available_permission_classes = ()
    create_data = {}

    def perform_update(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, "updated_by"):
            self.create_data["updated_by_id"] = self.request.user.id

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)

    # def perform_destroy(self, instance):
    #     # Customization destroy for change instance status instead of delete
    #     data = {"status": Status.INACTIVE}
    #     serializer = self.get_serializer(instance, data=data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     # check if the instance has validate_delete method available
    #     if hasattr(serializer.Meta.model, "validate_delete"):
    #         serializer.Meta.model.validate_delete(serializer.instance)
    #     self.perform_update(serializer)

    def add_extra_fields(self, extra_fields):
        for key in extra_fields:
            self.create_data[key] = extra_fields[key]

    # def get_queryset(self):
    #     return self.get_serializer_class().Meta.model.objects.filter(
    #         status=Status.ACTIVE
    #     )
