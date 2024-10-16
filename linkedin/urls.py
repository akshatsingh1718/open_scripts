# fetcher/urls.py
from django.urls import path
from .views import contribution_from_text, contribution_from_link, index

urlpatterns = [
    path("", index, name="index"),
    path("contrib-link/", contribution_from_link, name="contrib_link"),
    path("contrib-text/", contribution_from_text, name="contrib_text"),
]
