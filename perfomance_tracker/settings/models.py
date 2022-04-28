from django.db import models

# Create your models here.


class Setting(models.Model):
    stream = models.ForeignKey(
        'streams.Stream',
        on_delete=models.CASCADE,
        verbose_name='Поток'
    )
    required = models.PositiveSmallIntegerField(
        default=600,
        verbose_name='Кол-во баллов для допуска к зачёту/экзамену'
    )
    autopass = models.PositiveSmallIntegerField(
        default=1000,
        verbose_name='Кол-во баллов для экзамена/зачёта автоматом'
    )

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return f'Настройки потока {str(self.stream)}'
