from django.contrib import admin
from scores.models import Score

# Register your models here.


class ScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Score, ScoreAdmin)
