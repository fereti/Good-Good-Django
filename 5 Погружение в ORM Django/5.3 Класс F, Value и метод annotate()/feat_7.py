# Подвиг 7. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import F, Q, Value
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
# records = # здесь прописывайте команду
# Используя стандартный менеджер записей (objects) модели Person, классы F, Q и Value, сформировать выборку из сотрудников, возраст (age) которых меньше 35 или зарплата (salary) меньше 40000 с двумя дополнительными вычисляемыми полями:
#
# поле tax = salary * 0.13
# поле is_paid = False
# То есть, первое поле tax вычисляется на основе поля salary с умножением на 0.13, а второе поле is_paid всюду равно False (булевому значению).
#
# P.S. Порядок параметров в критерии и порядок полей не менять, сначала tax, затем is_paid. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import F, Q, Value


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.filter(Q(age__lt=35) | Q(salary__lt=40000)).annotate(tax=F("salary") * 0.13,
                                                                              is_paid=Value(False))
