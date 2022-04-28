# Generated by Django 4.0.4 on 2022-04-28 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('years', '0002_alter_year_options_alter_year_year'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Настройка', 'verbose_name_plural': 'Настройки'},
        ),
        migrations.AlterField(
            model_name='setting',
            name='autopass',
            field=models.PositiveSmallIntegerField(default=1000, verbose_name='Кол-во баллов для экзамена/зачёта автоматом'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='required',
            field=models.PositiveSmallIntegerField(default=600, verbose_name='Кол-во баллов для допуска к зачёту/экзамену'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='years.year', verbose_name='Поток'),
        ),
    ]
