# Подвиг 4. Пусть имеется следующий класс модели:
#
# from django.db import models
#
# class ShopItem(models.Model):
#     name = models.CharField(max_length=255)
#     descr = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_exists = models.BooleanField(default=True)
# Добавьте с помощью этого класса в таблицу новую запись товара с параметрами:
#
# name="Добрый, добрый Django 4"
# descr="Лучший курс по Django 4"
#
# путем создания экземпляра класса ShopItem с последующим вызовом нужного метода.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class ShopItem(models.Model):
    name = models.CharField(max_length=255)
    descr = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_exists = models.BooleanField(default=True)


ShopItem(name="Добрый, добрый Django 4", descr="Лучший курс по Django 4").save()
