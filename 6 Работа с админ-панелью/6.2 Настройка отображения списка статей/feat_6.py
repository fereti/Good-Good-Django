# Подвиг 6. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
#     class Meta:
#         verbose_name = 'Сотрудник'
#         verbose_name_plural = 'Сотрудники'
#
#
# # --------- admin.py ------------------------
# from django.contrib import admin
# # импорт from .models import Person
#
# # здесь продолжайте программу
# С помощью декоратора admin.register зарегистрируйте модель Person для админ-панели и примените его к новому классу PersonAdmin, унаследованного от базового класса admin.ModelAdmin. В классе PersonAdmin определите:
#
# отображаемые поля: full_name, salary, is_active;
# редактируемые поля: salary, is_active;
# порядок сортировки записей по возрастанию поля salary и убыванию поля age.
# Дополните модель Person так, чтобы поля full_name, salary, is_active в админ-панели отображались с соответствующими именами:
#
# Имя сотрудника; Зарплата; Работающий
#
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Имя сотрудника")
    salary = models.PositiveIntegerField(default=0, verbose_name="Зарплата")
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True, verbose_name="Работающий")

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# --------- admin.py ------------------------
from django.contrib import admin


# импорт from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "salary", "is_active")
    list_editable = ("salary", "is_active")
    ordering = ["salary", "-age"]
