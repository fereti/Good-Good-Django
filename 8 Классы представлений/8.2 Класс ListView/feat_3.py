# Подвиг 3 (усложнение подвига 2). Пусть имеется следующая модель:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
#
# # --------- views.py ------------------------
# from django.views.generic import ListView
# # from .models import Post
#
# # здесь продолжайте программу
# Объявите класс представления ListPost, унаследованного от класса ListView, со следующим функционалом:
#
# через атрибуты класса:
#
# шаблон для отображения статей: 'post/list.html';
# переменная со списком выбранных записей из модели Post (для передачи в шаблон): posts;
# дополнительные переменные для шаблона: {'title': "Список опубликованных статей"};
# через методы класса:
#
# метод для выборки записей из модели Post, у которых значение поля is_published равно 1 (через стандартный менеджер записей).
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# --------- views.py ------------------------
from django.views.generic import ListView


# from .models import Post

class ListPost(ListView):
    template_name = 'post/list.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Список опубликованных статей',
    }

    def get_queryset(self):
        return Post.objects.filter(is_published=True)
