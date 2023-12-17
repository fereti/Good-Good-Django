# Подвиг 1. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import F
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
# Используя стандартный менеджер записей (objects) модели Person и класс F, нужно увеличить зарплату (salary) всех сотрудников на 1000.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import F


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


Person.objects.update(salary=F("salary") + 1000)
