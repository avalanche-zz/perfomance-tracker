# Generated by Django 4.0.4 on 2022-04-28 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required', models.PositiveSmallIntegerField(default=600, verbose_name='Кол-во баллов для допуска к зачёту/экзамену')),
                ('autopass', models.PositiveSmallIntegerField(default=1000, verbose_name='Кол-во баллов для экзамена/зачёта автоматом')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streams.stream', verbose_name='Поток')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
