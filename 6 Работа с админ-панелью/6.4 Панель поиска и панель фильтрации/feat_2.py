# Подвиг 2. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Subject(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
#     name = models.CharField(max_length=255, verbose_name='Название')
#     volume_lect = models.PositiveIntegerField(default=0, verbose_name='Объем лекций')
#     volume_lab = models.PositiveIntegerField(default=0, verbose_name='Объем лабораторных')
#
#     class Meta:
#         verbose_name = 'Предмет'
#         verbose_name_plural = 'Предметы'
#
#
# # --------- admin.py ------------------------
# from django.contrib import admin
# # импорт from .models import Subject
#
# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'volume_lect', 'volume_lab']
#     # здесь продолжайте программу
# Добавьте в класс SubjectAdmin атрибуты для следующих настроек в админ-панели:
#
# редактируемые поля: volume_lect, volume_lab;
# кликабельные поля: name;
# упорядочивание: по убыванию поля volume_lect;
# поиск (через панель поиска админки): по полю name.
# P.S. На экран ничего выводить не нужно


# --------- models.py ------------------------
from django.db import models


class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    name = models.CharField(max_length=255, verbose_name='Название')
    volume_lect = models.PositiveIntegerField(default=0, verbose_name='Объем лекций')
    volume_lab = models.PositiveIntegerField(default=0, verbose_name='Объем лабораторных')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# --------- admin.py ------------------------
from django.contrib import admin


# импорт from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'volume_lect', 'volume_lab']
    list_editable = ('volume_lect', 'volume_lab')
    list_display_links = ['name', ]
    ordering = ('-volume_lect',)
    search_fields = ('name',)
