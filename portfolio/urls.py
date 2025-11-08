from django.urls import path
from .views import portfolio_list, portfolio_detail
urlpatterns = [
    path("", portfolio_list, name="portfolio_list"),
    path("<slug:slug>/", portfolio_detail, name="portfolio_detail"),
]
