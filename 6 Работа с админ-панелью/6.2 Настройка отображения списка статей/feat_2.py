# Подвиг 2. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Subject(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     name = models.CharField(max_length=255)
#     volume = models.PositiveIntegerField(default=0)
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
# # здесь продолжайте программу
# С помощью декоратора admin.register зарегистрируйте модель Subject для админ-панели и примените его к новому классу SubjectAdmin. В этом классе определите порядок сортировки отображаемых в админ-панели записей по убыванию поля volume.
#
# P.S. Не забудьте унаследовать класс SubjectAdmin от класса admin.ModelAdmin. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# --------- admin.py ------------------------
from django.contrib import admin


# импорт from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ordering = ("-volume",)
