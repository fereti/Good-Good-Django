#  Подвиг 3. Пусть в программе объявлена следующая модель:
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
# Используя стандартный менеджер записей (objects) модели Subject и метод aggregate(), вычислите среднее значение часов (volume) предметов, а также минимальную и максимальную цену (price). На выходе должен формироваться словарь с ключами: 'vol_avg', 'pr_min', 'pr_max' и соответствующими значениями.
#
# P.S. Порядок вызова агрегирующих функций, как указано в описании. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min


class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = Subject.objects.aggregate(vol_avg=Avg("volume"), pr_min=Min("price"), pr_max=Max("price"))
