# Generated by Django 4.1.4 on 2022-12-15 17:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Звание')),
            ],
        ),
        migrations.CreateModel(
            name='Solder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('birth_date', models.DateField(default=datetime.date(2000, 1, 1), verbose_name='Дата рождения')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soldiers.title', verbose_name='Звание')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]