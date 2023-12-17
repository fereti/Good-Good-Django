# Подвиг 6. Объявите в программе класс формы авторизации LoginUserForm, унаследованный от базового класса AuthenticationForm со следующими элементами:
#
# через атрибуты класса:
#
# username: текстовое поле ввода, максимальная длина 100, название "Логин", стили attrs={'class': 'form-input'};
# password: поле ввода пароля, максимальная длина 50, название "Пароль", стили attrs={'class': 'form-input'};
# через атрибуты вложенного класса Meta:
#
# модель формы: текущая модель пользователя, возвращенная функцией get_user_model();
# отображаемые поля в форме авторизации: username, password.
# Объявите класс представления LoginUser, унаследованный от базового класса LoginView, со следующими элементами:
#
# через атрибуты класса:
#
# форма для авторизации: LoginUserForm;
# шаблон для отображения формы: 'users/login.html';
# дополнительные параметры: {'title': "Авторизация пользователя"};
# через методы класса:
#
# перенаправление при успешной авторизации по маршруту с именем 'profile', используя функцию reverse_lazy.
# P.S. На экран ничего выводить не нужно.


# ------------------ forms.py -----------------------
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import get_user_model
from django import forms


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-input'}))

    password = forms.CharField(label='Пароль',
                               max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


# ------------------ views.py -----------------------
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
# from .forms import LoginUserForm

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация пользователя'}

    def get_success_url(self):
        return reverse_lazy('profile')
