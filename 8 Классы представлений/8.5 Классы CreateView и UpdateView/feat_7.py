# Подвиг 7. Пусть имеется следующий фрагмент программы:
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
# # --------- mgu/lector_delete.html-----------
# <form method="post">
#     {% csrf_token %}
#     <p>Удаляемая запись: "{{ object }}"</p>
#     {{ form.as_p }}
#     <input type="submit" value="Удалить">
# </form>
#
# # --------- views.py ------------------------
# from django.urls import reverse_lazy
# from django.views.generic.edit import DeleteView
# # from .models import Lector
#
# # здесь продолжайте программу
# Необходимо в разделе views.py объявить класс представления с именем DeleteLector, унаследованный от базового класса DeleteView, со следующим функционалом:
#
# через атрибуты класса:
#
# используемая модель: Lector;
# шаблон: 'mgu/lector_delete.html';
# перенаправление при успешном добавлении: reverse_lazy('lector-list').


# --------- models.py ------------------------
from django.db import models


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')


# --------- mgu/lector_delete.html-----------
# <form method="post">
#     {% csrf_token %}
#     <p>Удаляемая запись: "{{ object }}"</p>
#     {{ form.as_p }}
#     <input type="submit" value="Удалить">
# </form>

# --------- views.py ------------------------
# from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


# from .models import Lector

class DeleteLector(DeleteView):
    model = Lector
    template_name = 'mgu/lector_delete.html'
    success_url = reverse_lazy("lector-list")
