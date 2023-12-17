# Подвиг 4. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, blank=True, db_index=True)
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'категории'
#
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     is_published = models.BooleanField(default=True)
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
#
#     class Meta:
#         verbose_name = 'Статья'
#         verbose_name_plural = 'Статьи'
#
#
# # --------- admin.py ------------------------
# from django.contrib import admin
# # импорт from .models import Category, Post
#
# # здесь продолжайте программу
# Необходимо зарегистрировать для админ-панели модель Post и во вспомогательном классе PostAdmin (унаследованный от admin.ModelAdmin) определить:
#
# отображаемые поля: title, slug, cat;
# кликабельные поля: title;
# поиск (через панель поиска админки): по полю title и по полю name связанной модели Category;
# фильтрация записей: по полям is_published и name связанной модели Category.
# Дополнительно в модели Post для полей title, slug, cat прописать отображаемые в админ-панели соответствующие названия:
#
# "Заголовок", "Слаг", "Категория"
#
# P.S. На экран ничего выводить не нужно


# --------- models.py ------------------------
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin


# импорт from .models import Category, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'cat']
    list_display_links = ('title',)
    search_fields = ('title', 'cat__name',)
    list_filter = ('is_published', 'cat__name')
