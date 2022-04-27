from django.db import models

# Create your models here.


class Year(models.Model):
    year = models.DateField(unique=True)
