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
    )
    group = models.IntegerField()
    subgroup = models.CharField(max_length=5)
    education_type = models.IntegerField(choices=EDUCATION_TYPE_CHOICES)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['year', 'group', 'subgroup', 'education_type'],
                name='unique_group'
            )
        ]
