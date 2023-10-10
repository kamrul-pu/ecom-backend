"""
Our apps custom permissions will be added here.
"""

from rest_framework.permissions import BasePermission, SAFE_METHODS

from core.choices import UserKind


from rest_framework.permissions import BasePermission


class IsUserKind(BasePermission):
    def __init__(self, allowed_user_kind):
        self.allowed_user_kind = allowed_user_kind

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.kind == self.allowed_user_kind


class IsSuperAdmin(IsUserKind):
    def __init__(self):
        super().__init__(UserKind.SUPER_ADMIN)


class IsAdminUser(IsUserKind):
    def __init__(self):
        super().__init__(UserKind.ADMIN)


class IsDistributor(IsUserKind):
    def __init__(self):
        super().__init__(UserKind.DISTRIBUTOR)


class IsDeliveryMan(IsUserKind):
    def __init__(self):
        super().__init__(UserKind.DELIVERY_MAN)


class IsCustomer(IsUserKind):
    def __init__(self):
        super().__init__(UserKind.CUSTOMER)


class IsBuyer(IsUserKind):
    def __init__(self):
        super().__init__(UserKind.BUYER)


class IsAutenticatedOrReadOnly(IsUserKind):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (
            request.user.is_authenticated and super().has_permission(request, view)
        ):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or (
            request.user.is_authenticated
            and super().has_object_permission(request, view, obj)
        )


# class IsSuperAdmin(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.kind == UserKind.SUPER_ADMIN:
#             return True
#         return False


# class IsAdminUser(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.kind == UserKind.ADMIN:
#             return True
#         return False


# class IsDistributor(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.kind == UserKind.DISTRIBUTOR:
#             return True
#         return False


# class IsDeliveryMan(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.kind == UserKind.DELIVERY_MAN:
#             return True
#         return False


# class IsCustomer(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.kind == UserKind.CUSTOMER:
#             return True
#         return False


# class IsBuyer(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.kind == UserKind.BUYER:
#             return True
#         return False
