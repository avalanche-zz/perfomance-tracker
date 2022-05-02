from django.contrib import admin
from .models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
