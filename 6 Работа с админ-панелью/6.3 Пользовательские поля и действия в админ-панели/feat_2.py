# Подвиг 2. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
#     title = models.CharField(max_length=255, verbose_name='Заголовок')
#     content = models.TextField(blank=True, verbose_name='Контент')
#     is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
#
#     class Meta:
#         verbose_name = 'Статья'
#         verbose_name_plural = 'Статьи'
#
#
# # --------- admin.py ------------------------
# from django.contrib import admin
# # импорт from .models import Post
#
# # здесь продолжайте программу
# Необходимо зарегистрировать для админ-панели модель Post и во вспомогательном классе PostAdmin (унаследованный от admin.ModelAdmin) определить:
#
# отображаемые поля: title, slug, is_published, + поля методов;
# кликабельные поля: title.
# Затем, добавить пользовательское вычисляемое поле путем объявления в классе PostAdmin метода:
#
# def info_post(self, post: Post): ...
# Который должен возвращать число слов в заголовке title в виде фразы:
#
# "Заголовок содержит <число> слов"
#
# (Полагается, что слова разделяются пробелом.)
#
# Добавьте поле созданного метода info_post для отображения в админ-панели. Декорируйте метод info_post, чтобы в админ-панели это поле имело название "О заголовке".
#
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin


# импорт from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'info_post')
    list_display_links = ('title',)

    @admin.display(description='О заголовке')
    def info_post(self, post: Post):
        count_w = len(post.title.split())
        return f"Заголовок содержит {count_w} слов"
