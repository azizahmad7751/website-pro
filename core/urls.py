from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("services/", include("pages.urls_services")),
    path("about/", include("pages.urls_about")),
    path("portfolio/", include("portfolio.urls")),
    path("careers/", include("careers.urls")),
    path("contact/", include("contact.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
