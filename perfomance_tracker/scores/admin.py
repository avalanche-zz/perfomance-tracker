from django.contrib import admin
from .models import Score

# Register your models here.


class ScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Score, ScoreAdmin)
