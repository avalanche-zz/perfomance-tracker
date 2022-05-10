from django.contrib import admin
from .models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Имя',
            {
                'fields': [
                    'last_name',
                    'first_name',
                    'patronymic'
                ]
            }
        )
    ]
    search_fields = [
        'last_name',
        'first_name',
        'patronymic'
    ]


admin.site.register(Teacher, TeacherAdmin)
