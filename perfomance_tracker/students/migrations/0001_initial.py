# Generated by Django 4.0.4 on 2022-04-28 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('vk_link', models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на ВК')),
                ('git_link', models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на GitHub/GitLab')),
                ('acquired_achievements', models.ManyToManyField(blank=True, related_name='acquired_by_students', to='achievements.achievement', verbose_name='Полученные достижения')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group', verbose_name='Группа')),
                ('promised_achievements', models.ManyToManyField(blank=True, related_name='promised_to_students', to='achievements.achievement', verbose_name='Обещанные достижения')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
