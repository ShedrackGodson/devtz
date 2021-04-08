from django.urls import path
from devs.views import (
    index, settings, password, change_password,
    delete_account, social_auths, preferences,
    save_dev_preference, email_notifications,
    save_email_preference, stacks, profile,
    add_other_experience, delete_other_experience,
    update_other_experience, add_certificate,
    save_availability
)


urlpatterns = [
    path("", index, name="home"),
    path('settings/', settings, name='settings'),
    path('settings/password/', password, name='password'),
    path('settings/password/<int:dev_id>/change-password/', change_password,
         name='change_password'),
    path('settings/<int:dev_id>/delete-account/',
         delete_account, name='delete_account'),
    path('settings/social-auths/', social_auths, name='social_auths'),
    path('settings/preferences/', preferences, name='preferences'),
    path('settings/preferences/dev/<int:dev_id>/save/', save_dev_preference,
         name='save_dev_preference'),
    path('settings/email-notifications/',
         email_notifications, name='email_notifications'),
    path('settings/email-notifications/<int:dev_id>/save/', save_email_preference,
         name='save_email_preference'),
    path('settings/stacks/', stacks, name='stacks'),
    # Profile
    path('devs/@<str:username>/', profile, name='profile'),
    path('devs/@<str:username>/add/', add_other_experience,
         name='add_other_experience'),
    path('devs/<int:experience_id>/@<str:dev_username>/delete/',
         delete_other_experience, name='delete_other_experience'),
    path('devs/<int:experience_id>/@<str:dev_username>/update/',
         update_other_experience, name='update_other_experience'),
    path('devs/@<str:dev_username>/add/',
         add_certificate, name='add_certificate'),
    path('devs/@<str:dev_username>/availability/save/',
         save_availability, name='save_availability'),
]
