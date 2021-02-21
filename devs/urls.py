from django.urls import path
from devs.views import (
    index, settings, password
)


urlpatterns = [
    path("", index, name="home"),
    path('settings/', settings, name='settings'),
    path('settings/password/', password, name='password'),
]

