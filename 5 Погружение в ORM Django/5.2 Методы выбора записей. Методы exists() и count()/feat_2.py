# Подвиг 2. Пусть в программе объявлена следующая модель:
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
# Используя стандартный менеджер записей (objects) модели Post, путем вызова одного из методов first/last (подумайте какого), выберите запись с наименьшим (самым ранним) временем создания (поле time_create).
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


record = Post.objects.last()
