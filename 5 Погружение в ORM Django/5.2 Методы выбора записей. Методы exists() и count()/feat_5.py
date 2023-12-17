# Подвиг 5. Пусть в программе объявлена следующая модель:
#
# from django.db import models
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['-time_create']
#
#
# record = # здесь продолжайте команду
# Используя стандартный менеджер записей (objects) модели Post, сформируйте сначала выборку всех записей с упорядочиванием по возрастанию поля slug (с помощью метода order_by), а затем, из полученного списка выберите запись с наименьшим временем изменения (поле time_update) с помощью одного из методов latest/earliest.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = Post.objects.order_by("slug").earliest("time_update")
