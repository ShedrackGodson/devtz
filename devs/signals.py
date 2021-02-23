from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from devs.models import (
    DeletedDev, Dev, EmailPreference, PublicPreference
)


@receiver(pre_delete, sender=Dev)
def deleted_dev_accounts(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=Dev)
def create_public_preferences(sender, instance, created, **kwargs):
    if created:
        object = PublicPreference()
        object.dev = instance
        object.save()
        print("Public Preference Created For ", instance)


@receiver(post_save, sender=Dev)
def email_preferences(sender, instance, created, **kwargs):
    if created:
        object = EmailPreference()
        object.dev = instance
        object.save()
        print("Email Preference Created For ", instance)

