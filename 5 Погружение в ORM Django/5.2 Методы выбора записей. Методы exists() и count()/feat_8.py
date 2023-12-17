#  Подвиг 8. Пусть в программе объявлена следующая модель:
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
# Используя стандартный менеджер записей (objects) модели Post, метод filter() и класс Q, выберите из таблицы записи по критерию: slug содержит фрагмент 'django' и title содержит фрагмент 'django' (оба без учета регистра). Определите наличие хотя бы одной записи в полученной выборке. На выходе нужно получить значение True, если записи есть, и False в противном случае.
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


result = Post.objects.filter(Q(slug__icontains="django") & Q(title__icontains="django")).exists()
