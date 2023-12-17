# Подвиг 3. Пусть имеется следующий фрагмент программы:
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
# Необходимо дополнить модель Subject так, чтобы поля slug, name, volume в админ-панели отображались с соответствующими именами:
#
# Слаг; Название; Объем
#
# Затем, зарегистрируйте эту модель в админ-панели с помощью декоратора admin.site.register.
#
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    name = models.CharField(max_length=255, verbose_name="Название")
    volume = models.PositiveIntegerField(default=0, verbose_name="Объем")

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# --------- admin.py ------------------------
from django.contrib import admin

# импорт from .models import Subject

admin.site.register(Subject)
