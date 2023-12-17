# Подвиг 6. Пусть имеется следующая модель:
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
# from django.views.generic.edit import UpdateView
# # from .models import Lector
#
# # здесь продолжайте программу
# Необходимо в разделе views.py объявить класс представления с именем UpdateLector, унаследованный от базового класса UpdateView, со следующим функционалом:
#
# через атрибуты класса:
#
# используемая модель: Lector;
# поля для редактирования в форме: fio, slug, salary, is_work;
# шаблон: 'mgu/lector_create.html';
# перенаправление при успешном добавлении: reverse_lazy('lector-list');
# дополнительные переменные для шаблона: {'title': 'Добавление лектора'}.
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
from django.views.generic.edit import UpdateView


# from .models import Lector

class UpdateLector(UpdateView):
    model = Lector
    fields = '__all__'
    template_name = 'mgu/lector_create.html'
    success_url = reverse_lazy('lector-list')
    extra_context = {
        'title': 'Добавление лектора'
    }
