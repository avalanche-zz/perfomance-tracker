from django.contrib import admin
from years.models import Year

# Register your models here.


class YearAdmin(admin.ModelAdmin):
    pass


admin.site.register(Year, YearAdmin)
