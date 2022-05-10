from django.contrib import admin
from .models import Stream
from groups.models import Group

# Register your models here.


class GroupInline(admin.TabularInline):
    model = Group
    extra = 0
    classes = [
        'collapse'
    ]


class StreamAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            'Поток',
            {
                'fields': [
                    'stream'
                ]
            }
        ),
        (
            'Настройки',
            {
                'fields': [
                    'required',
                    'autopass'
                ],
                'classes': [
                    'collapse'
                ]
            }
        )
    ]
    inlines = [
        GroupInline
    ]
    search_fields = [
        'stream'
    ]


admin.site.register(Stream, StreamAdmin)
