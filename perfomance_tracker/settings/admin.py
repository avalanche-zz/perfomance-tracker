from django.contrib import admin
from settings.models import Setting

# Register your models here.


class SettingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Setting, SettingAdmin)
