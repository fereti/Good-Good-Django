# Подвиг 2. Пусть имеется следующая модель:
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
#     objects = models.Manager()
#     model_manager = ModelManager()
# Объявите в программе пользовательский класс менеджера ModelManager, который бы возвращал все статьи со значением is_published равным 1 и заголовком (title), начинающимся с фрагмента "ли" (регистронезависимый).
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


# здесь объявляйте класс менеджера
class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True, title__istartswith='ли')


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    model_manager = ModelManager()
