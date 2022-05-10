from django.contrib import admin
from .models import Group
from students.models import Student

# Register your models here.


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0
    fields = [
        'last_name',
        'first_name',
        'patronymic'
    ]
    classes = [
        'collapse'
    ]


class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Информация о группе',
            {
                'fields': [
                    'stream',
                    'group',
                    'subgroup',
                    'education_type'
                ]
            }
        )
    ]
    inlines = [
        StudentInline
    ]
    list_filter = [
        'stream',
        'education_type'
    ]

admin.site.register(Group, GroupAdmin)
