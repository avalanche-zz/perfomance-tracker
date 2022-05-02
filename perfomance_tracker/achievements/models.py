from django.db import models
from students.models import Student, StudentAchievements

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

    # Automatically attach the just-created achievement
    # to every existing student with "doesn't have" relation
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            for student_to_be_attached_to in Student.objects.all():
                StudentAchievements.objects.create(
                    student=student_to_be_attached_to,
                    achievement=self,
                    relation=0
                )

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
