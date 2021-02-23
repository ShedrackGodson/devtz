from django.contrib import admin
from devs.models import (
    DeletedDev, Dev, PublicPreference,
    EmailPreference
)

admin.site.register(Dev)
admin.site.register(DeletedDev)
admin.site.register(PublicPreference)
admin.site.register(EmailPreference)
