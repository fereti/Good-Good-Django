# Подвиг 4. Пусть в программе объявлена модель и форма для нее:
#
# # ---------------- models.py -------------------------
# from django.db import models
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#
# # ---------------- forms.py -------------------------
# from django import forms
# # from .models import Category
#
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'slug']
#
# # ---------------- views.py -------------------------
# # from django.shortcuts import render
# # from .models import Category
# # from .forms import CategoryForm
#
# # здесь продолжайте программу
# Объявите в программе функцию представления с именем add_category и пропишите в ней следующий функционал:
#
# для метода передачи данных GET представление должно создавать пустую форму CategoryForm и с помощью функции render формируется HTML-документ по шаблону 'subject/addcategory.html' с передачей в него объекта формы CategoryForm через переменную (ключ) form;
# при получении POST-запроса создать заполненную форму CategoryForm (из принятых данных), проверить корректность заполнения формы стандартным методом формы и для корректных данных выполнить сохранение данных формы в БД (с помощью соответствующего метода формы); после сохранения данных возвратить объект формы.
# P.S. На экран ничего выводить не нужно.


# ---------------- models.py -------------------------
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


# ---------------- forms.py -------------------------
from django import forms


# from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']


# ---------------- views.py -------------------------
# from django.shortcuts import render
# from .models import Category
# from .forms import CategoryForm

def add_category(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'subject/addcategory.html', {'form': form})
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return form
