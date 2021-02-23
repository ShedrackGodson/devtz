from django.contrib.auth.models import AbstractUser
from django.db import models


class Dev(AbstractUser):
    email = models.EmailField(('email address'), blank=True, unique=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(upload_to="devs/", null=True, blank=True)
    website_link = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(
        ("male", "Male"),
        ("female", "Female"),
    ), null=True, blank=True)
    hireable = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self) -> str():
        return self.email

    class Meta:
        ordering = [
            "-id"
        ]

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['city', 'phone','username']


class DeletedDev(Dev):
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> None:
        return None
    
    class Meta:
        ordering = (
            "-id",
        )


class PublicPreference(models.Model):
    dev = models.OneToOneField(Dev, on_delete=models.CASCADE)
    both_emails = models.BooleanField(default=False)
    hireable = models.BooleanField(default=False)
    bio = models.BooleanField(default=True)
    phone = models.BooleanField(default=True)
    gender = models.BooleanField(default=False)

    def __str__(self):
        return self.dev.email
    
    class Meta:
        ordering = (
            "-id",
        )

class EmailPreference(models.Model):
    dev = models.OneToOneField(Dev, on_delete=models.CASCADE)
    logins = models.BooleanField(default=False)
    updates = models.BooleanField(default=False)
    messages = models.BooleanField(default=True)
    
    def __str__(self):
        return self.dev.email
    
    class Meta:
        ordering = (
            "-id",
        )