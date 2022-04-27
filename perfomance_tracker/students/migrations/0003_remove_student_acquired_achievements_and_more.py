# Generated by Django 4.0.4 on 2022-04-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
        ('students', '0002_rename_group_id_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='acquired_achievements',
        ),
        migrations.AddField(
            model_name='student',
            name='acquired_achievements',
            field=models.ManyToManyField(related_name='acquired_by_students', to='achievements.achievement'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='promised_achievements',
        ),
        migrations.AddField(
            model_name='student',
            name='promised_achievements',
            field=models.ManyToManyField(related_name='promised_to_students', to='achievements.achievement'),
        ),
    ]
