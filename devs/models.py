from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.db import models


class Dev(AbstractUser):
    email = models.EmailField(('email address'), blank=True, unique=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    pay_rate = models.FloatField(default=0.0, null=True, blank=True)
    profile_image = models.ImageField(upload_to="devs/", null=True, blank=True)
    website_link = models.CharField(max_length=255, null=True, blank=True)
    bio = RichTextField(max_length=2500, null=True, blank=True)
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
    REQUIRED_FIELDS = ['city', 'phone', 'username']


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


class VideoIntroduction(models.Model):
    dev = models.OneToOneField(Dev, on_delete=models.CASCADE)
    youtube_link = models.CharField(max_length=500)

    def __str__(self):
        return self.dev.email

    class Meta:
        ordering = (
            "-id",
        )


class Availability(models.Model):
    dev = models.OneToOneField(Dev, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    days_available = models.CharField(max_length=20, choices={
        ("more", "More than 30 hrs/week"),
        ("les", "Less than 30 hrs/week"),
        ("open", "As needed - open to offers"),
    })

    def __str__(self):
        return self.dev.email

    class Meta:
        ordering = (
            "-id",
        )


class Language(models.Model):
    dev = models.ForeignKey(Dev, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices={
        ("basic", "I write in this language decently"),
        ("conversational", "I write and speak this language well"),
        ("fluent", "I write and speak this language almost perfectly"),
        ("native", "I write and speak this language perfectly, including colloquilisms"),
    })

    def __str__(self):
        return self.dev.email

    class Meta:
        ordering = (
            "-id",
        )


class Education(models.Model):
    dev = models.ForeignKey(Dev, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    date_from = models.IntegerField()
    date_to = models.IntegerField()

    def __str__(self):
        return self.dev.email

    class Meta:
        ordering = (
            "-id",
        )


class SkillSet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices={
        ("language", "Programming Language"),
        ("framework", "Framework"),
        ("other", "Other"),
    })
    description = RichTextField(max_length=5000,
                                null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = (
            "-id",
        )


class DevSkillSet(models.Model):
    dev = OneToOneField(Dev, on_delete=models.CASCADE)
    skill_sets = models.ManyToManyField(SkillSet)

    def __str__(self):
        return self.dev.email

    class Meta:
        ordering = (
            "-id",
        )


class DevCertificates(models.Model):
    dev = ForeignKey(Dev, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    description = RichTextField(max_length=255, null=True, blank=True)
    issue_date = models.DateField()
    expiration = models.DateField(null=True, blank=True)
    certificate_id = models.CharField(max_length=100,
                                      null=True, blank=True)
    certificate_url = models.CharField(max_length=100,
                                       null=True, blank=True)

    def __str__(self):
        return self.dev.email

    class Meta:
        ordering = (
            "-id",
        )


class DevEmploymentHistory(models.Model):
    dev = ForeignKey(Dev, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    from_month = models.CharField(max_length=10)
    from_year = models.CharField(max_length=4)
    to_month = models.CharField(max_length=10,
                                null=True, blank=True)
    to_year = models.CharField(max_length=4,
                               null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = RichTextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.dev.email

    class Meta:
        ordering = (
            "-id",
        )


class OtherExperience(models.Model):
    dev = ForeignKey(Dev, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = RichTextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.dev.email

    class Meta:
        ordering = (
            "-id",
        )
