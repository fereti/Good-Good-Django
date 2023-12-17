# Подвиг 4. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255, verbose_name='Имя')
#     salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
#     age = models.PositiveIntegerField(default=0, verbose_name='Возраст')
#     job = models.CharField(max_length=255, verbose_name='Профессия')
#     is_active = models.BooleanField(default=True)
#
# # --------- views.py ------------------------
# from django.views.generic import ListView
# # from .models import Person
#
# # здесь объявляйте класс PersonList
# Объявите класс представления PersonList в разделе views.py, унаследованного от класса ListView, со следующим функционалом:
# через атрибуты класса:
#
# шаблон для отображения статей: 'person/list.html';
# переменная со списком выбранных записей из модели Person (для передачи в шаблон): persons;
# запрет на отображение страницы без записей (должно генерироваться исключение 404);
# через методы класса:
#
# метод формирования (для шаблона) переменной title со значением "Список персон";
# метод для выборки записей: с помощью стандартного менеджера записей модели Person и метода filter выбрать все записи, у которых поле salary в пределах [11000; 32000] (включительно).
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст')
    job = models.CharField(max_length=255, verbose_name='Профессия')
    is_active = models.BooleanField(default=True)


# --------- views.py ------------------------
from django.views.generic import ListView


# from .models import Person

class PersonList(ListView):
    template_name = 'person/list.html'
    context_object_name = 'persons'
    allow_empty = False

    def get_queryset(self):
        queryset = Person.objects.filter(salary__range=[11000, 32000])
        if not queryset:
            raise Http404
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список персон'
        return context
