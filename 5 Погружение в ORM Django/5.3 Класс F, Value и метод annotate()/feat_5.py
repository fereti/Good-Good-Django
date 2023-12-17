#  Подвиг 5. Пусть в программе объявлена следующая модель:
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
# Используя стандартный менеджер записей (objects) модели Person, классы F и Q, сформировать выборку из сотрудников, у которых возраст (age) больше 40 или зарплата (salary) больше 20000. Для этой выборки дополнительно сформировать вычисляемое поле tax (налог) на основе поля salary по следующей формуле: tax = salary*0.13
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


records = Person.objects.filter(Q(age__gt=40) | Q(salary__gt=20000)).annotate(tax=F("salary") * 0.13)
