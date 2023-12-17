# Подвиг 7. Пусть имеется следующий класс модели:
#
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
# Используя метод filter() стандартного менеджера записей класса Person, выберите все записи с параметром salary строго меньше 20000.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


Person.objects.filter(salary__lt=20000)
