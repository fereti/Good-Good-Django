#  Подвиг 8. Пусть имеются две следующие модели:
#
# from django.db import models
# from django.db.models import Count, Sum, Avg, Max, Min
#
# class Subject(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     name = models.CharField(max_length=255)
#     volume = models.PositiveIntegerField(default=0)
#
#
# class Lector(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     fio = models.CharField(max_length=255)
#     subjects = models.ManyToManyField('Subject', blank=True, related_name='subs')
# Используя стандартный менеджер записей (objects) модели Lector, выполните группировку по предметам (subjects) с определением общего числа лекторов и при условии, что предмет volume >= 16. Новое вычисляемое поле с числом лекторов назвать total. Агрегирующая функция Count() должна применяться к полю id.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min


class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    fio = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', blank=True, related_name='subs')


result = Lector.objects.filter(subjects__volume__gte=16).annotate(total=Count('id')).values('subjects', 'total')
