# Подвиг 5. Пусть имеется следующий класс модели:
#
# # --------------- models.py -------------------------
# class Subject(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     name = models.CharField(max_length=255)
#     volume = models.PositiveIntegerField(default=0)
#
# # --------------- forms.py -------------------------
# # from .models import Subject
#
# # здесь продолжайте программу
# Объявите класс формы с именем LectorForm, не связанной с моделью, со следующими полями:
#
# first_name: текстовое поле; максимальная длина 100 символов, обязательное, название "Имя";
# last_name: текстовое поле; максимальная длина 100 символов, обязательное, название "Фамилия";
# email: поле ввода адреса электронной почты; обязательное, название "E-mail";
# salary: числовое поле; необязательное, название "Зарплата";
# subject: поле выбора из модели Subject; обязательное, название "Предмет", название не выбранного пункта "Выберите предмет".
#
# Атрибуты класса должны иметь те же названия и порядок, что и в описании.
#
# P.S. На экран ничего выводить не нужно.


# --------------- models.py -------------------------
from django.db import models


class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


# --------------- forms.py -------------------------
# from .models import Subject

class LectorForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, label='Имя')
    last_name = forms.CharField(max_length=100, required=True, label='Фамилия')
    email = forms.EmailField(required=True, label='E-mail')
    salary = forms.IntegerField(required=False, label='Зарплата')
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=True, label='Предмет',
                                     empty_label='Выберите предмет')
