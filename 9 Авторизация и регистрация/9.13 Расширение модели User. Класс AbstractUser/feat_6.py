# Подвиг 6. Пусть имеется следующая расширенная модель пользователя:
#
# # from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# class Lector(AbstractUser):
#     avatar = models.ImageField(upload_to="avatars/%Y/%m/", blank=True, verbose_name="Изображение")
#     status = models.CharField(max_length=200, blank=True, verbose_name="Должность")
#     salary = models.IntegerField(blank=True, default=0, verbose_name="Зарплата")
# Объявите класс формы ProfileForm для редактирования профиля пользователя (форма связанная с моделью) со следующими элементами:
#
# через атрибуты класса:
#
# username: текстовое поле, закрытое для редактирования (disabled=True), название "Логин";
# email: поле ввода E-mail, закрытое для редактирования (disabled=True), название "E-mail";
# status: текстовое поле, закрытое для редактирования (disabled=True), название "Должность";
# через атрибуты вложенного класса Meta:
#
# модель: получить через вызов функции get_user_model();
# отображаемые поля в форме (порядок важен): avatar, username, email, first_name, last_name, status, salary;
# дополнительные названия полей: first_name -> "Имя", last_name -> "Фамилия".
# P.S. На экран ничего выводить не нужно.


# from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class Lector(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/%Y/%m/", blank=True, verbose_name="Изображение")
    status = models.CharField(max_length=200, blank=True, verbose_name="Должность")
    salary = models.IntegerField(blank=True, default=0, verbose_name="Зарплата")


class ProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')
    email = forms.EmailField(disabled=True, label='E-mail')
    status = forms.CharField(disabled=True, label='Должность')

    class Meta:
        model = get_user_model()
        fields = ['avatar', 'username', 'email', 'first_name', 'last_name', 'status', 'salary']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
