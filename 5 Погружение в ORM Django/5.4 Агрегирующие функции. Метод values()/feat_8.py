# Подвиг 8 (на повторение). Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import Q
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
# Используя стандартный менеджер записей (objects) модели Person, измените значение поля is_active на False (булево значение) у записей с salary < 10000 или age > 65.
#
# P.S. Порядок следования критериев отбора записей, как в описании. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Q


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    
Person.objects.filter(Q(salary__lt=10000) | Q(age__gt=65)).update(is_active=False)
