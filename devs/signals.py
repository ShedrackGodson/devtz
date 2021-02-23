from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from devs.models import (
    DeletedDev, Dev, EmailPreference, PublicPreference, SkillSet
)

import wikipediaapi


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


@receiver(post_save, sender=SkillSet)
def fetch_wikipedia_api(sender, instance, created, **kwargs):
    if created:
        wiki = wikipediaapi.Wikipedia('en')
        skill_name = instance.name
        if instance.type == "language":
            page = wiki.page(f'{skill_name}_(programming_language)')
        elif instance.type == "framework":
            page = wiki.page(f'{skill_name}_(web_framework)')
        try:
            fetch = page.exists() # Consume wikipedia endpoint
            if fetch:
                instance.description = page.summary
        except ConnectionError:
            pass
        instance.save()

