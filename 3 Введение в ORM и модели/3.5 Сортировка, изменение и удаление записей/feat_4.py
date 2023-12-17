# Подвиг 4. Пусть имеется следующий класс модели:
#
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
# Добавьте в него вложенный класс с именем Meta и пропишите автоматическую сортировку выбираемых записей по возрастанию зарплаты salary.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)

    class Meta:
        ordering = ['salary']
