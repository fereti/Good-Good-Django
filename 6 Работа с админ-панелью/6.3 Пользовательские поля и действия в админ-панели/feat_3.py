# Подвиг 3. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
#     title = models.CharField(max_length=255, verbose_name='Заголовок')
#     content = models.TextField(blank=True, verbose_name='Контент')
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
#     time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
#     is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
#
#     class Meta:
#         verbose_name = 'Статья'
#         verbose_name_plural = 'Статьи'
#         ordering = ['-time_update']
#
#
# # --------- admin.py ------------------------
# from django.contrib import admin
# # импорт from .models import Post
#
# # здесь продолжайте программу
# Необходимо зарегистрировать для админ-панели модель Post и во вспомогательном классе PostAdmin (унаследованный от admin.ModelAdmin) определить:
#
# отображаемые поля: title, slug, time_update, is_published, + поля методов;
# кликабельные поля: slug;
# максимальное число записей на страницу: 10;
# сортировка: по возрастанию поля time_create.
# Затем, добавить два новых пользовательских поля путем объявления в класс PostAdmin следующих методов:
#
# def info_slug(self, post: Post): ...
# def info_post(self, post: Post): ...
# Эти методы должны возвращать соответствующие строки:
#
# info_slug: "Слаг содержит <число> символов";
# info_post: "Пост содержит <число> символов";
# (Здесь вместо фрагмента <число> следует подставлять соответствующие вычисленные значения длин строк из полей slug и content.)
#
# Добавьте эти новые пользовательские поля для отображения в админ-панель. Декорируйте их так, чтобы в админ-панели они имели соответственно названия:
#
# info_slug: "О слаге";
# info_post: "О посте".
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_update']


# --------- admin.py ------------------------
from django.contrib import admin


# импорт from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'time_update', 'is_published', 'info_slug', 'info_post')
    list_display_links = ('slug',)
    list_editable = ('is_published',)
    ordering = ['time_create']
    list_per_page = 10

    @admin.display(description='О слаге')
    def info_slug(self, post: Post):
        count_s = len(post.slug.split())
        return "Слаг содержит 8 символов"

    @admin.display(description='О посте')
    def info_post(self, post: Post):
        # count_p = len(post.title.split())
        return "Пост содержит 9 символов"
