# Generated by Django 4.0.4 on 2022-04-29 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
        ('students', '0002_relation_remove_student_acquired_achievements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievements.achievement'),
        ),
        migrations.AddConstraint(
            model_name='relation',
            constraint=models.UniqueConstraint(fields=('student', 'achievement'), name='unique_student_achievement_relation'),
        ),
    ]
