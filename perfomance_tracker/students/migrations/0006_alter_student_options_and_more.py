# Generated by Django 4.0.4 on 2022-04-28 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0002_alter_achievement_options_and_more'),
        ('groups', '0003_alter_group_options_alter_group_education_type_and_more'),
        ('students', '0005_alter_student_acquired_achievements_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterField(
            model_name='student',
            name='acquired_achievements',
            field=models.ManyToManyField(blank=True, related_name='acquired_by_students', to='achievements.achievement', verbose_name='Полученные достижения'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='git_link',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на GitHub/GitLab'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='student',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='student',
            name='promised_achievements',
            field=models.ManyToManyField(blank=True, related_name='promised_to_students', to='achievements.achievement', verbose_name='Обещанные достижения'),
        ),
        migrations.AlterField(
            model_name='student',
            name='vk_link',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на ВК'),
        ),
    ]
