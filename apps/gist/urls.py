from django.urls import re_path
from .views import GistView

app_name = "gist"

urlpatterns = [
    re_path("", GistView.as_view(), name="gist-list"),
]
