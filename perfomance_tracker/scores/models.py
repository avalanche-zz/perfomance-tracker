from datetime import date
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Score(models.Model):

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
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'Оценка студента {str(self.student).split()[0]} {str(self.student).split()[1][0]}. за работу "{str(self.assignment)}"'

    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    assignment = models.ForeignKey(
        'assignments.Assignment',
        on_delete=models.CASCADE,
        verbose_name='Задание'
    )
    general_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100)
        ],
        verbose_name='Оценка за работу'
    )
    deadline_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100)
        ],
        verbose_name='Оценка за дедлайн'
    )
    handing_in_date = models.DateField(
        default=date.today,
        verbose_name='Дата сдачи работы'
    )
