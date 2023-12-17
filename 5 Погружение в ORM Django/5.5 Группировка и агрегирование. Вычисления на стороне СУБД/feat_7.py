# Подвиг 7. Пусть имеются две следующие модели:
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
# Используя стандартный менеджер записей (objects) модели Subject, методы annotate() и filter(), выберите все записи (предметы), у которых имеется хотя бы один лектор. Общее число лекторов по каждому предмету хранить в вычисляемом поле с именем total.
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


result = Subject.objects.annotate(total=Count("subs")).filter(total__gt=0)
