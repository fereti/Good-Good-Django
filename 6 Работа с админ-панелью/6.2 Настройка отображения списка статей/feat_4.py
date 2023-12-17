# Подвиг 4. Пусть имеется следующий фрагмент программы:
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
# отображаемые поля: full_name, salary, job;
# редактируемые поля: salary;
# кликабельные поля: full_name.
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# --------- admin.py ------------------------
from django.contrib import admin


# импорт from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "salary", "job")
    list_editable = ("salary",)
    list_display_links = ("full_name",)
