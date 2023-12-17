# Подвиг 2. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import Count, Sum, Avg, Max, Min
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
#
# result = # здесь прописывайте команду
# Используя стандартный менеджер записей (objects) модели Person, вычислите количество записей для каждой профессии (job). Число записей должно храниться в поле с именем total. Агрегирующая функция Count() должна применяться к полю id.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = Person.objects.values("job").annotate(total=Count("id"))
