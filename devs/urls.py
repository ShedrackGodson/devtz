from django.urls import path
from devs.views import index, login


urlpatterns = [
    path("", index, name="home"),
    path("login/", login, name="login"),
]

