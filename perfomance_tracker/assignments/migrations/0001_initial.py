# Generated by Django 4.0.4 on 2022-05-19 12:21

import assignments.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('deadline', models.DateField(default=assignments.models.default_deadline, verbose_name='Дедлайн')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streams.stream', verbose_name='Поток')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.AddConstraint(
            model_name='assignment',
            constraint=models.UniqueConstraint(fields=('name', 'description', 'deadline', 'stream'), name='unique_assignment'),
        ),
    ]
