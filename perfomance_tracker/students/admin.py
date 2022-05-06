from django.contrib import admin
from .models import Student, StudentAchievement
from scores.models import Score

# Register your models here.


class StudentAchievementInline(admin.TabularInline):
    model = StudentAchievement
    exta = 0
    fields = [
        'achievement',
        'relation'
    ]
    classes = [
        'collapse'
    ]


class ScoreInline(admin.TabularInline):
    model = Score
    extra = 0
    fileds = [
        'assignment',
        'general_score',
        'deadline_score',
        'handing_in_date'
    ]
    classes = [
        'collapse'
    ]


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Информация о имени',
            {
                'fields': [
                    'last_name',
                    'first_name',
                    'patronymic'
                ]
            }
        ),
        (
            'Группа',
            {
                'fields': [
                    'group'
                ]
            }
        ),
        (
            'Ссылки',
            {
                'fields': [
                    'vk_link',
                    'git_link'
                ],
                'classes': [
                    'collapse'
                ]
            }
        )
    ]
    inlines = [
        StudentAchievementInline,
        ScoreInline
    ]


admin.site.register(Student, StudentAdmin)
