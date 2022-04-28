from django.db import models

# Create your models here.


class Year(models.Model):
    year = models.DateField(
        unique=True,
        verbose_name='Год зачисления',
        help_text='Формат: yyyy-01-01, где yyyy (например, 2021) – год зачисления'
    )

    class Meta:
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'
