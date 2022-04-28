from django.db import models

# Create your models here.


class Assignment(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    deadline = models.DateField(
        verbose_name='Дедлайн'
    )
    assigned_to_year = models.ForeignKey(
        'years.Year',
        on_delete=models.CASCADE,
        verbose_name='Поток'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'description', 'deadline', 'assigned_to_year'],
                name='unique_assignment'
            )
        ]
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
