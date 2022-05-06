from django.contrib import admin
from .models import Assignment
from scores.models import Score

# Register your models here.


class ScoreInline(admin.TabularInline):
    model = Score
    extra = 0
    fields = [
        'student',
        'general_score',
        'deadline_score',
        'handing_in_date'
    ]
    classes = [
        'collapse'
    ]


class AssignmentAdmin(admin.ModelAdmin):
    inlines = [
        ScoreInline
    ]


admin.site.register(Assignment, AssignmentAdmin)
