from django.db import models

# Create your models here.


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'description', 'image'],
                name='unique_achievement'
            )
        ]
