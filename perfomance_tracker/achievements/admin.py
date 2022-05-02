from django.contrib import admin
from .models import Achievement

# Register your models here.


class AchievementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Achievement, AchievementAdmin)
