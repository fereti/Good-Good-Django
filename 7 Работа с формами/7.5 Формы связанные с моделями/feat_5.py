# Подвиг 5. Пусть в программе объявлена следующая модель:
#
# # ---------------- models.py -------------------------
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255, verbose_name="Полное имя")
#     salary = models.PositiveIntegerField(default=0, verbose_name="Зарплата")
#     age = models.PositiveIntegerField(default=0, verbose_name="Возраст")
#     job = models.CharField(max_length=255, verbose_name="Профессия")
#     is_active = models.BooleanField(default=True, verbose_name="Статус")
#
# # ---------------- forms.py -------------------------
# from django import forms
# # from .models import Person
#
# # здесь продолжайте программу
# Объявите класс формы AddPersonForm, связанной с моделью Person со следующими свойствами, прописанными во вложенном классе Meta:
#
# отображаемые поля (с сохранением порядка): full_name, age, job;
# поля full_name, age и job должны иметь CSS-стили attrs={'class': 'form-input'}.
# Добавить в класс AddPersonForm метод с именем:
#
# clean_<проверяемое поле>
#
# для проверки, что введенный возраст age меньше 65. Если проверка не проходит, то генерировать исключение:
#
# raise ValidationError("Слишком большой возраст.")
# Иначе, метод должен возвращать значение age.
#
# P.S. На экран ничего выводить не нужно.


# ---------------- models.py -------------------------
from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное имя")
    salary = models.PositiveIntegerField(default=0, verbose_name="Зарплата")
    age = models.PositiveIntegerField(default=0, verbose_name="Возраст")
    job = models.CharField(max_length=255, verbose_name="Профессия")
    is_active = models.BooleanField(default=True, verbose_name="Статус")


# ---------------- forms.py -------------------------
from django import forms
from django.core.exceptions import ValidationError


# from .models import Person

class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'age', 'job']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'age': forms.TextInput(attrs={'class': 'form-input'}),
            'job': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age >= 65:
            raise forms.ValidationError("Слишком большой возраст.")
        return age
