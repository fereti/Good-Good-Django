# Подвиг 6. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models.functions import Length
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
# Используя стандартный менеджер записей (objects) модели Post, методы annotate(), filter() и count(), определите число записей с размером заголовка (title) больше 50 символов. Размер заголовка должен определяться полем length.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models
from django.db.models.functions import Length


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    
    
result = Post.objects.annotate(length=Length('title')).filter(length__gt=50).count()
