from datetime import date, timedelta
from django.db import models

# Create your models here.

def default_deadline():
    return date.today() + timedelta(weeks=4)

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
        default=default_deadline,
        verbose_name='Дедлайн'
    )
    stream = models.ForeignKey(
        'streams.Stream',
        on_delete=models.CASCADE,
        verbose_name='Поток'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'description', 'deadline', 'stream'],
                name='unique_assignment'
            )
        ]
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.name
