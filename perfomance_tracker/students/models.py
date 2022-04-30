from django.db import models

# Create your models here.


class Student(models.Model):

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'.strip()

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
    achievements = models.ManyToManyField(
        'achievements.Achievement',
        through='StudentAchievements'
    )

class StudentAchievements(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'achievement'],
                name='unique_student-achievement_relation'
            )
        ]

    RELATION_CHOICES=(
        (0, 'Не обещано/выдано'),
        (1, 'Обещано'),
        (2, 'Выдано')
    )
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    achievement=models.ForeignKey(
        'achievements.Achievement',
        on_delete=models.CASCADE
    )
    relation=models.PositiveSmallIntegerField(
        choices=RELATION_CHOICES,
        verbose_name='Отношение'
    )
