from django.contrib import admin
from .models import Stream

# Register your models here.


class StreamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stream, StreamAdmin)
