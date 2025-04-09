from django.urls import re_path
from .views import JobsView

app_name = "jobs"

urlpatterns = [
    re_path("", JobsView.as_view(), name="jobs-list"),
]
