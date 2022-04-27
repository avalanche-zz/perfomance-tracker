from django.contrib import admin
from groups.models import Group

# Register your models here.


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
