# Подвиг 4. Пусть имеется следующий класс модели:
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
# Используя стандартный менеджер записей (objects) модели Person, с помощью метода filter() выберите все записи по критерию: is_active = 1 и salary > 12000.
#
# P.S. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Q


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = Person.objects.filter(Q(is_active=1) & Q(salary__gt=12000))
