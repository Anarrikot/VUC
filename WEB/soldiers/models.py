from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

class Solder(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50)
    number = models.CharField(verbose_name='Номер телефона', max_length=50)
    birth_date = models.DateField(verbose_name='Дата рождения', default=date(2000, 1, 1))
    title = models.ForeignKey('Title', on_delete=models.CASCADE, verbose_name='Звание', null=True)
    slug = models.SlugField(verbose_name='URL', max_length=255,unique=True, db_index=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return  self.last_name
    def get_absolute_url(self):
        return reverse('solder', kwargs={'so_slug': self.slug})

class Title(models.Model):
    name = models.CharField(verbose_name='Звание', max_length=50)
    def __str__(self):
        return f'{self.name}'