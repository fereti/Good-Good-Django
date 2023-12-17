# Подвиг 10. Пусть имеется следующий класс модели:
#
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
# Используя метод get() стандартного менеджера записей класса Person, выберите запись с параметром pk равным 3.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


Person.objects.get(pk=3)
