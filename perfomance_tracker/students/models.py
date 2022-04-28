from django.db import models

# Create your models here.


class Student(models.Model):
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    patronymic = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Отчество'
    )
    group = models.ForeignKey(
        'groups.Group',
        on_delete=models.CASCADE,
        verbose_name='Группа'
    )
    vk_link = models.URLField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Ссылка на ВК'
    )
    git_link = models.URLField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Ссылка на GitHub/GitLab'
    )
    promised_achievements = models.ManyToManyField(
        'achievements.Achievement',
        blank=True,
        related_name='promised_to_students',
        verbose_name='Обещанные достижения'
    )
    acquired_achievements = models.ManyToManyField(
        'achievements.Achievement',
        blank=True,
        related_name='acquired_by_students',
        verbose_name='Полученные достижения'
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
