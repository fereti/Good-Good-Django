# Подвиг 5. Пусть имеется следующая модель:
#
# class Post(models.Model):
#     class Status(models.TextChoices):
#         DRAFT = 'drf', 'Черновик'
#         PUBLISHED = 'pub', 'Опубликовано'
#
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = # здесь определяйте поле CharField с перечислением Status
# Вам необходимо дописать атрибут is_published, который должен определять текстовое поле максимальной длины 3, использовать перечисление Status и по умолчанию принимать значение атрибута PUBLISHED класса Status.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import TextChoices


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'drf', 'Черновик'
        PUBLISHED = 'pub', 'Опубликовано'

    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.CharField(max_length=3, choices=Status.choices, default=Status.PUBLISHED)
