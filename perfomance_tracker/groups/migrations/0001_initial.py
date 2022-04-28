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
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.PositiveSmallIntegerField(verbose_name='Номер группы')),
                ('subgroup', models.CharField(max_length=5, verbose_name='Подгруппа')),
                ('education_type', models.IntegerField(choices=[(0, 'Очное'), (1, 'Заочное')], verbose_name='Тип обучения')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streams.stream', verbose_name='Поток')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.AddConstraint(
            model_name='group',
            constraint=models.UniqueConstraint(fields=('stream', 'group', 'subgroup', 'education_type'), name='unique_group'),
        ),
    ]
