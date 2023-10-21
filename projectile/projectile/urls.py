"""
Main URL Mapping of the app.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # user related urls
    path("api/v1/users", include("core.rest.urls.users")),
    path("api/v1/me", include("core.rest.urls.me")),
    path("api/v1/auth", include("core.rest.urls.auth")),
    # include jwt authentication
    path("api/v1/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify", TokenVerifyView.as_view(), name="token_verify"),
    # Product related urls
    path(
        "api/v1/products", include("product.rest.urls.base"), name="product-base-urls"
    ),
    path("api/v1/orders", include("order.rest.urls.base"), name="order-base-urls"),
    path(
        "api/v1/addresses", include("address.rest.urls.base"), name="address-base-urls"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularSwaggerView,
    )

    urlpatterns += [
        path("api/schema", SpectacularAPIView.as_view(), name="schema"),
        # Optional UI:
        path(
            "api/docs",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
if settings.ENABLE_SILK:
    urlpatterns += [re_path(r"^profiler/", include("silk.urls", namespace="silk"))]
