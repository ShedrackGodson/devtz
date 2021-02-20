from django.contrib.auth.models import AbstractUser
from django.db import models


class Dev(AbstractUser):
    email = models.EmailField(('email address'), blank=True, unique=True)
    profile_image = models.ImageField(upload_to="devs/", null=True, blank=True)
    website_link = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(
        ("male", "Male"),
        ("female", "Female"),
    ), null=True, blank=True)
    hireable = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = [
            "-id"
        ]

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['city', 'mobile_phone','username']

