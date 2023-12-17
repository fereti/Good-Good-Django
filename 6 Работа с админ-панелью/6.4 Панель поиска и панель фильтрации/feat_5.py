# Подвиг 5. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     is_published = models.BooleanField(default=True)
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
#
# class ContentFilter(admin.SimpleListFilter):
#     # здесь прописывайте атрибуты title и parameter_name
#
#     def lookups(self, request, model_admin):
#         # здесь продолжайте метод lookups
#
#     def queryset(self, request, queryset):
#         # здесь продолжайте метод queryset
#
#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug', 'is_published']
#     list_display_links = ['title']
#     list_filter = ['is_published', ContentFilter]
# Необходимо дописать класс ContentFilter, который бы определял фильтрацию постов по объему их контента (поле content) в соответствии со следующими критериями (для отбора записей используйте метод annotate для формирования вычисляемого поля с именем length и последующим вызовом метода filter):
#
# Короткие статьи: content < 1000 символов;
# Средние статьи: 1000 <= content < 5000 символов;
# Большие статьи: content >= 5000 символов.
# Названия пунктов в фильтре: "Короткие статьи", "Средние статьи", "Большие статьи". Названия параметров соответственно:
#
# short, middle, long.
#
# Атрибуты title и parameter_name класса ContentFilter определить следующими:
#
# title = "Сортировка по статьям"
# parameter_name = 'status'
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
from django.db.models.functions import Length


# импорт from .models import Post


class ContentFilter(admin.SimpleListFilter):
    title = "Сортировка по статьям"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ("short", "Короткие статьи"),
            ("middle", "Средние статьи"),
            ("long", "Большие статьи")
        ]

    def queryset(self, request, queryset):
        if self.value() == "short":
            return queryset.annotate(length=Length('content')).filter(length__lt=1000)
        elif self.value() == "middle":
            return queryset.annotate(length=Length('content')).filter(length__gte=1000, length__lt=5000)
        elif self.value() == "long":
            return queryset.annotate(length=Length('content')).filter(length__gte=5000)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published']
    list_display_links = ['title']
    list_filter = ['is_published', ContentFilter]
