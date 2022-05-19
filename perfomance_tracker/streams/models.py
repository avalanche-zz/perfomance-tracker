from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Stream(models.Model):

    class Meta:
        ordering = [
            'stream'
        ]
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'

    def __str__(self):
        return str(self.stream)

    stream = models.PositiveSmallIntegerField(
        unique=True,
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(2099)
        ],
        verbose_name='Год зачисления'
    )
    required = models.PositiveSmallIntegerField(
        default=600,
        verbose_name='Кол-во баллов для допуска к зачёту/экзамену'
    )
    autopass = models.PositiveSmallIntegerField(
        default=1000,
        verbose_name='Кол-во баллов для экзамена/зачёта автоматом'
    )
