from django.contrib import admin
from .models import Score

# Register your models here.


class ScoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'student',
                    'assignment'
                ]
            }
        ),
        (
            'Оценка',
            {
                'fields': [
                    'general_score',
                    'deadline_score'
                ]
            }
        ),
        (
            None,
            {
                'fields': [
                    'handing_in_date'
                ]
            }
        )
    ]


admin.site.register(Score, ScoreAdmin)
