# Подвиг 5 (на повторение). Пусть имеется следующий класс модели:
#
# from django.db import models
# from django.db.models import Q
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
#
# p_lst = # здесь продолжайте команду
# Используя стандартный менеджер записей (objects) модели Person, с помощью метода filter() и класса Q выберите все записи по критерию: is_active = 0 или salary < 10000.
#
# P.S. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Q


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = Person.objects.filter(Q(is_active=0) | Q(salary__lt=10000))
