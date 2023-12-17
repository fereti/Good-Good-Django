#  Подвиг 2. Пусть в программе объявлена следующая модель:
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
# Используя стандартный менеджер записей (objects) модели Person, классы F и Q, нужно увеличить зарплату (salary) в 2 раза всех сотрудников у которых поле job равно 'django' или возраст (age) больше 30.
#
# P.S. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import F, Q


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


Person.objects.filter(Q(job='django') | Q(age__gt=30)).update(salary=F('salary') * 2)
