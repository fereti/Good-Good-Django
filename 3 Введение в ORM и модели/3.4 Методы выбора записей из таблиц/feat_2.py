# Подвиг 2. Пусть имеется следующий класс модели:
#
# from django.db import models
#
# class CourseItem(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
# Добавьте с помощью этого класса в таблицу две записи с параметрами:
#
# title="Курс по Django 4"
# content="Полный базовый курс по Django 4"
# и
#
# title="Добрый, добрый Django 4"
# content="Курс по Django 4 на Stepik"
# Сделать это следует с помощью вызова метода create менеджера записей класса CourseItem.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


CourseItem.objects.create(title="Курс по Django 4", content="Полный базовый курс по Django 4")
CourseItem.objects.create(title="Добрый, добрый Django 4", content="Курс по Django 4 на Stepik")
