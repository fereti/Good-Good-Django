# Подвиг 2. Объявите класс формы LectorRegisterForm на базе класса UserCreationForm со следующими элементами:
#
# через атрибуты класса:
#
# username: текстовое поле, максимальная длина 50 символов, название "Логин", CSS-стили attrs={'class': 'form-input'};
# password1: поле ввода пароля, максимальная длина 30 символов, название "Пароль", CSS-стили attrs={'class': 'form-input'};
# password2: поле ввода пароля, максимальная длина 30 символов, название "Повтор пароля", CSS-стили attrs={'class': 'form-input'};
# через атрибуты вложенного класса Meta:
#
# модель: определяется вызовом функции get_user_model();
# отображаемые в форме поля: username, first_name, last_name, email, password1, password2;
# дополнительные метки (названия) полей: first_name -> "Имя", last_name -> "Фамилия", email -> "E-mail".
# P.S. На экран ничего выводить не нужно.


from django import forms


# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

class LectorRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль',
                                max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                                max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'E-mail',
        }
