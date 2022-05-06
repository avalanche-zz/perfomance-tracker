from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.


def validate_format(value):
    if value.month != 1 or value.day != 1:
        raise ValidationError(
            _(f'{value} is formatted incorrectly (Accepted format: 20yy-01-01)'),
            params={'value': value},
        )


class Stream(models.Model):

    class Meta:
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'

    def __str__(self):
        return str(self.stream.year)

    stream = models.DateField(
        unique=True,
        validators=[
            MinValueValidator(date(2000, 1, 1)),
            MaxValueValidator(date(2099, 1, 1)),
            validate_format
        ],
        verbose_name='Год зачисления',
        help_text='Формат: 20yy-01-01, где 20yy (например, 2021) – год зачисления'
    )
    required = models.PositiveSmallIntegerField(
        default=600,
        verbose_name='Кол-во баллов для допуска к зачёту/экзамену'
    )
    autopass = models.PositiveSmallIntegerField(
        default=1000,
        verbose_name='Кол-во баллов для экзамена/зачёта автоматом'
    )
