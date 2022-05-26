from django.contrib import admin
# Register your models here.
from .models import *

#ignore this
# class RectifyAdmin(admin.ModelAdmin):
#     fields = ['store', 'report', 'status', 'issue', 'covid_compliance']

admin.site.register(NonFBReport)
admin.site.register(FBReport)
admin.site.register(CovidReport)
admin.site.register(Store)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(NonFBChecklist)
admin.site.register(Announcement)
admin.site.register(CovidComplianceChecklist)
admin.site.register(FBChecklist)
admin.site.register(AuditScore)