# Подвиг 6. Пусть имеется следующий класс модели:
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
# Используя стандартный менеджер записей (objects) модели Person, с помощью метода filter() и класса Q выберите все записи по критерию: job != 'junior' или salary >= 40000.
#
# P.S. Помните о приоритетах операций. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Q


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = Person.objects.filter(~Q(job="junior") | Q(salary__gte=40000))
