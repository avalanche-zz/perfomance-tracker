from django.db import models

# Create your models here.


class Student(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    group = models.ForeignKey(
        'groups.Group',
        on_delete=models.CASCADE,
    )
    vk_link = models.CharField(max_length=250, blank=True)
    git_link = models.CharField(max_length=250, blank=True)
    promised_achievements = models.CharField(max_length=500, blank=True)
    acquired_achievements = models.CharField(max_length=500, blank=True)
