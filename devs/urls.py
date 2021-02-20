from django.urls import path
from devs.views import index


urlpatterns = [
    path("", index, name="home"),
]

