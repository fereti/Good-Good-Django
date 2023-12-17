# Подвиг 1. Пусть имеется следующий класс модели:
#
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
# Добавьте с помощью этого класса в таблицу новую запись с параметрами:
#
# full_name="Сергей Балакирев"
# salary=4321
# job="Создатель"
#
# Сделать это следует с помощью вызова метода create менеджера записей класса Person.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


Person.objects.create(full_name="Сергей Балакирев", salary=4321, job='Создатель')
