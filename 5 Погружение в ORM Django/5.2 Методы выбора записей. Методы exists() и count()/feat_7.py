#  Подвиг 7. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import Q
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
# Используя стандартный менеджер записей (objects) модели Post, метод filter() и класс Q, выберите из таблицы записи по критерию: slug содержит фрагмент 'django' или фрагмент 'python' (без учета регистра). Определите число записей в полученной выборке.
#
# P.S. Все нужно записать в виде одной команды (строчки). Порядок параметров в критерии не менять. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Q


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


result = Post.objects.filter(Q(slug__icontains="django") | Q(slug__icontains="python")).count()
