# Подвиг 6. Пусть в программе объявлена следующая модель:
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
#
# result = # здесь продолжайте команду
# Используя стандартный менеджер записей (objects) модели Post, выберите из таблицы записи по критерию: is_published = 0. Определите наличие хотя бы одной записи в полученной выборке. На выходе нужно получить значение True, если записи есть, и False в противном случае.
#
# P.S. Все нужно записать в виде одной команды (строчки). На экран ничего выводить не нужно.


from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


result = Post.objects.filter(is_published=0).exists()
