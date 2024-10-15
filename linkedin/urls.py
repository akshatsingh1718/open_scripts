# fetcher/urls.py
from django.urls import path
from .views import contribution_from_text, contribution_from_link

urlpatterns = [
    path("contrib-link/", contribution_from_link, name="contrib_link"),
    path("contri-text/", contribution_from_text, name="contrib_text"),
]
