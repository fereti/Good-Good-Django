# Подвиг 4. Пусть имеется следующий фрагмент программы:
#
# # --------------- models.py ---------------------------------------
# from django.db import models
#
# class Lector(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
#     fio = models.CharField(max_length=255, verbose_name='ФИО')
#     salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
#     photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name='Изображение')
#     is_work = models.BooleanField(default=False, verbose_name='Статус')
#
# # --------------- forms.py ---------------------------------------
# from django import forms
# #from .models import Lector
#
# class LectorForm(forms.ModelForm):
#     class Meta:
#         model = Lector
#         fields = ['fio', 'slug', 'photo', 'salary']
#
# # --------------- views.py ---------------------------------------
# # from django.shortcuts import render, redirect
# # from .forms import LectorForm
#
# # здесь определяйте функцию представления
# Необходимо объявить функцию представления add_lector со следующим функционалом:
#
# при GET-запросе должна создаваться пустая форма LectorForm и с помощью функции render формироваться HTML-документ по шаблону 'profile/add_lector.html' с передачей в него объекта формы LectorForm через переменную (ключ) form;
# при POST-запросе должна формироваться заполненная форма LectorForm, затем, выполняться проверка корректности переданных данных методом is_valid, при успешной проверке данные формы сохраняются в БД и выполняется редирект на главную страницу с помощью команды:
# return redirect('/')
# P.S. На экран ничего выводить не нужно.


# --------------- models.py ---------------------------------------
from django.db import models


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name='Изображение')
    is_work = models.BooleanField(default=False, verbose_name='Статус')


# --------------- forms.py ---------------------------------------
from django import forms


# from .models import Lector

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['fio', 'slug', 'photo', 'salary']


# --------------- views.py ---------------------------------------
# from django.shortcuts import render, redirect
# from .forms import LectorForm

def add_lector(request):
    if request.method == 'GET':
        form = LectorForm()
        return render(request, 'profile/add_lector.html', {'form': form})
    elif request.method == 'POST':
        form = LectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
