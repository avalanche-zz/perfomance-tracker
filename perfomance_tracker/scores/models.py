from datetime import date
from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator

# Create your models here.


class Score(models.Model):
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
    )
    assignment = models.ForeignKey(
        'assignments.Assignment',
        on_delete=models.CASCADE,
    )
    general_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100)
        ]
    )
    deadline_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100)
        ]
    )
    handing_in_date = models.DateField(default=date.today)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'student_id', 'assignment_id', 'general_score',
                    'deadline_score', 'handing_in_date'
                ],
                name='unique_score'
            )
        ]
