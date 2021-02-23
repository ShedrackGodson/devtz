from django.contrib import admin
from devs.models import (
    DeletedDev, Dev, PublicPreference,
    EmailPreference, VideoIntroduction, Availability,
    Language, Education, SkillSet, DevSkillSet,
    DevCertificates, DevEmploymentHistory,
    OtherExperience
)

admin.site.register(Dev)
admin.site.register(DeletedDev)
admin.site.register(PublicPreference)
admin.site.register(EmailPreference)
admin.site.register(VideoIntroduction)
admin.site.register(Availability)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(SkillSet)
admin.site.register(DevSkillSet)
admin.site.register(DevCertificates)
admin.site.register(DevEmploymentHistory)
admin.site.register(OtherExperience)

