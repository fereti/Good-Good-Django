# Подвиг 5. Пусть имеется следующая модель:
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
# # --------- views.py ------------------------
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
# # from .models import Lector
#
# # здесь продолжайте программу
# Необходимо в разделе views.py объявить класс представления с именем CreateLector, унаследованный от базового класса CreateView, со следующим функционалом:
#
# через атрибуты класса:
#
# используемая модель: Lector;
# поля для заполнения в форме: fio, slug, is_work;
# шаблон: 'mgtu/lector_create.html';
# перенаправление при успешном добавлении: reverse_lazy('lector-list');
# через методы класса:
#
# form_valid: назначить полю salary создаваемой записи значение 11000;
# Подсказка: ранее в подвиге был пример реализации метода form_valid, который здесь вам поможет:
#
# def form_valid(self, form):
#     p = form.save(commit=False)  # формирование объекта записи, без сохранения ее в БД (commit=False)
#     p.job = 'djano'              # изменение поля job на значение 'django'
#     return super().form_valid(form)  # запись сохраняется в БД через вызов метода form_valid базового класса
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')


# --------- views.py ------------------------
# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from .models import Lector

# здесь продолжайте программу
