# Generated by Django 4.0.4 on 2022-05-19 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'ordering': ['stream', 'name'], 'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
    ]
