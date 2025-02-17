from django.urls import re_path
from .views import CountriesView

app_name = "countries"

urlpatterns = [
    re_path("", CountriesView.as_view(), name="countries-list"),
]
