from django.contrib import admin
from .models import Achievement
from students.models import StudentAchievement

# Register your models here.


class StudentAchievementInline(admin.TabularInline):
    verbose_name_plural = 'Студенты'
    model = StudentAchievement
    extra = 0
    fields = [
        'student',
        'relation'
    ]
    classes = [
        'collapse'
    ]


class AchievementAdmin(admin.ModelAdmin):
    inlines = [
        StudentAchievementInline
    ]


admin.site.register(Achievement, AchievementAdmin)
