# Generated by Django 4.0.4 on 2022-04-27 14:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_rename_assignment_id_score_assignment_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='score',
            name='general_score_lte_100',
        ),
        migrations.RemoveConstraint(
            model_name='score',
            name='deadline_score_lte_100',
        ),
        migrations.AlterField(
            model_name='score',
            name='deadline_score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='score',
            name='general_score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
