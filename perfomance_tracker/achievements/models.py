from django.db import models

# Create your models here.


class Achievement(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'description', 'image'],
                name='unique_achievement'
            )
        ]
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    image = models.ImageField(
        blank=True,
        verbose_name='Изображение'
    )
