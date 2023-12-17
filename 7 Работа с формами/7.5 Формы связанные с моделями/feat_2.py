# Подвиг 2. Пусть в программе объявлена следующая модель:
#
# # ---------------- models.py -------------------------
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
#
# # ---------------- forms.py -------------------------
# from django import forms
# # from .models import Person
#
# # здесь продолжайте программу
# Объявите класс формы PersonForm, связанной с моделью Person и следующими свойствами, прописанными во вложенном классе Meta:
#
# отображаемые поля (с сохранением порядка): full_name, salary, job;
# поля full_name и job должны иметь CSS-стили attrs={'class': 'form-input'};
# названия полей в HTML-форме: full_name -> "Полное имя"; salary -> "Зарплата"; job -> "Профессия".
# P.S. На экран ничего выводить не нужно.


# ---------------- models.py -------------------------
from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


# ---------------- forms.py -------------------------
from django import forms


# from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'salary', 'job']
        labels = {
            'full_name': 'Полное имя',
            'salary': 'Зарплата',
            'job': 'Профессия'
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'job': forms.TextInput(attrs={'class': 'form-input'}),
        }
