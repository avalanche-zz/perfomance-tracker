from django.db import models

# Create your models here.
class Setting(models.Model):
    year = models.ForeignKey(
        'years.Year',
        on_delete=models.CASCADE,
    )
    required = models.PositiveSmallIntegerField(default=600)
    autopass = models.PositiveSmallIntegerField(default=1000)
