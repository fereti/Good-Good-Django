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
# Используя стандартный менеджер записей (objects) модели Post, путем вызова методов order_by() и first() выберите запись с наибольшим временем изменения (поле time_update).
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


record = Post.objects.order_by("-time_update").first()



