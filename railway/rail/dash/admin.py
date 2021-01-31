from django.contrib import admin
import dash.models as dm
# Register your models here.
admin.site.register(dm.profile)
admin.site.register(dm.train)
admin.site.register(dm.ticket)