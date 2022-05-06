from django.db import models

# Create your models here.


class Group(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'stream',
                    'group',
                    'subgroup',
                    'education_type'
                ],
                name='unique_group'
            )
        ]
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        if self.education_type:
            return f'ЗКИ{str(self.stream)[-2:]}-{self.group}/{self.subgroup}'
        return f'КИ{str(self.stream)[-2:]}-{self.group}/{self.subgroup}'

    EDUCATION_TYPE_CHOICES = (
        (0, 'Очное'),
        (1, 'Заочное')
    )
    stream = models.ForeignKey(
        'streams.Stream',
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
    education_type = models.PositiveSmallIntegerField(
        choices=EDUCATION_TYPE_CHOICES,
        verbose_name='Тип обучения'
    )
