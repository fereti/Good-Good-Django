# Подвиг 4. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import F, Q
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
# records = # здесь прописывайте команду
# Используя стандартный менеджер записей (objects) модели Person и класс F, сформировать выборку с дополнительным вычисляемым полем tax (налог), значение которого должно вычисляться на основе поля salary следующим образом: tax = salary*0.13
# P.S. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import F, Q


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.all().annotate(tax=F("salary") * 0.13)
