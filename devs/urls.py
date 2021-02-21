from django.urls import path
from devs.views import (
    index, login, create_dev
)


urlpatterns = [
    path("", index, name="home"),
    # path("login/", login, name="login"),
    # path("create_dev/", create_dev, name="create_dev"),
]

