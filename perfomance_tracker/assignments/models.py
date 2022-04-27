from django.db import models

# Create your models here.


class Assignment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    deadline = models.DateField()
    assigned_to_year = models.ForeignKey(
        'years.Year',
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'description', 'deadline', 'assigned_to_year'],
                name='unique_assignment'
            )
        ]
