from django.urls import path
from devs.views import (
    index, settings, password, change_password
)


urlpatterns = [
    path("", index, name="home"),
    path('settings/', settings, name='settings'),
    path('settings/password/', password, name='password'),
    path('settings/password/<int:dev_id>/change-password/', change_password, name='change_password'),
]

