# Подвиг 4. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Lector(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
#     fio = models.CharField(max_length=255, verbose_name='ФИО')
#     salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
#     is_work = models.BooleanField(default=False, verbose_name='Статус')
#
#     class Meta:
#         verbose_name = 'Лектор'
#         verbose_name_plural = 'Лекторы'
#
#
# # --------- admin.py ------------------------
# from django.contrib import admin
# # импорт from .models import Lector
#
# # здесь продолжайте программу
# Необходимо зарегистрировать для админ-панели модель Lector и во вспомогательном классе LectorAdmin (унаследованный от admin.ModelAdmin) определить:
#
# отображаемые поля: fio, salary, is_work, + поля методов;
# кликабельные поля: fio;
# редактируемые поля: is_work;
# максимальное число записей на страницу: 15.
# Дополнительно в классе LectorAdmin определить пользовательское поле со следующими характеристиками:
#
# название метода: info_salary;
# возвращаемое значение (в виде строки):
# "низкая", если salary < 25000;
# "средняя", если 25000 <= salary < 55000;
# "высокая", если salary >= 55000;
# название поля при отображении: "Величина зарплаты";
# сортировка поля: по убыванию поля salary.
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО', )
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'


# --------- admin.py ------------------------
from django.contrib import admin


# импорт from .models import Lector

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ("fio", "salary", "is_work", "info_salary")
    list_display_links = ('fio',)
    list_editable = ('is_work',)
    list_per_page = 15

    @admin.display(description='Величина зарплаты', ordering="-salary")
    def info_salary(self, obj):
        if obj.salary < 25000:
            return "низкая"
        elif 25000 <= obj.salary < 55000:
            return "средняя"
        else:
            return "высокая"
