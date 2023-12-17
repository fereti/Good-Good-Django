# Подвиг 4. На основе базового класса AuthenticationForm объявите новый класс формы с именем UserLoginForm со следующими элементами:
#
# через атрибуты класса:
#
# username: текстовое поле ввода, максимум 100 символов, обязательное, наименование "Логин";
# password: поле ввода пароля, максимум 50 символов, обязательное, наименование "Пароль".
# P.S. На экран ничего выводить не нужно.


# from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                               max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
