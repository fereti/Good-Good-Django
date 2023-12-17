# Подвиг 3. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.urls import reverse
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
# # --------- views.py ------------------------
# from django.urls import reverse_lazy
# from django.views.generic import ListView
# # from .models import Person
#
# def show_persons(request):
#     data = {
#         'title': 'Список персон',
#         'p_list': Person.objects.all(),
#     }
#
#     return render(request, 'users/persons.html', context=data)
# Замените функцию show_persons эквивалентным классом представления ShowPersons, унаследованным от базового класса ListView, со следующим функционалом (через атрибуты класса):
#
# шаблон: 'users/persons.html';
# модель: Person;
# переменная со списком записей (в шаблоне): p_list;
# дополнительные переменные: {'title': 'Список персон'};
# пагинация: разбиение по 3 записи на страницу.
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


# --------- views.py ------------------------
from django.views.generic import ListView


# from .models import Person

class ShowPersons(ListView):
    template_name = 'users/persons.html'
    model = Person
    context_object_name = 'p_list'
    paginate_by = 3
    extra_context = {
        'title': 'Список персон'
    }
