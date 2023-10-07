"""
Main URL Mapping of the app.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.ENABLE_SILK:
    print("profiler path")
    urlpatterns += [re_path(r"^profiler/", include("silk.urls", namespace="silk"))]
