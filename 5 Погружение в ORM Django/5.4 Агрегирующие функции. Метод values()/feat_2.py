# Подвиг 2. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import Count, Sum, Avg, Max, Min
#
# class Subject(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     name = models.CharField(max_length=255)
#     volume = models.PositiveIntegerField(default=16)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#
#
# result = # здесь прописывайте команду
# Используя стандартный менеджер записей (objects) модели Subject и метод aggregate(), вычислите среднее значение цены (price) предметов. На выходе должен формироваться словарь с ключом 'subject_avg' и соответствующим значением.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min


class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = Subject.objects.aggregate(subject_avg=Avg("price"))
