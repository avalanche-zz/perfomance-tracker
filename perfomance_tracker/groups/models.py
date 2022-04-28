from django.db import models

# Create your models here.


class Group(models.Model):
    EDUCATION_TYPE_CHOICES = (
        (0, 'Очное'),
        (1, 'Заочное')
    )
    year = models.ForeignKey(
        'years.Year',
        on_delete=models.CASCADE,
        verbose_name='Поток'
    )
    group = models.PositiveSmallIntegerField(
        verbose_name='Номер группы'
    )
    subgroup = models.CharField(
        max_length=5,
        verbose_name='Подгруппа'
    )
    education_type = models.IntegerField(
        choices=EDUCATION_TYPE_CHOICES,
        verbose_name='Тип обучения'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['year', 'group', 'subgroup', 'education_type'],
                name='unique_group'
            )
        ]
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
