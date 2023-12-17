# Подвиг 4. Объявите класс формы с именем LoginForm, не связанной с моделью, со следующими полями:
#
# username: текстовое поле; максимальная длина 50 символов, минимальная длина 5 символов, обязательное, название "Логин";
# password: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Пароль".
#
# Атрибуты класса должны иметь те же названия и порядок, что и в описании.
#
# Для полей формы через параметр widget укажите стили оформления: attrs={'class': 'form-login-input'}
#
# Для проверки корректности поля password объявите в классе LoginForm метод с именем:
#
# clean_<название поля>
#
# В этом методе реализовать проверку значения поля password по следующим критериям:
#
# допустимые символы: буквы латинского алфавита (малые и большие), цифры и символы "-?!$#@_";
# минимальная длина пароля 6 символов.
# Если эти проверки не проходят, то генерировать исключение:
#
# raise ValidationError("Некорректно введенный пароль.")
# Иначе метод должен возвращать введенный пароль (в виде строки).
#
# P.S. На экран ничего выводить не нужно.


from django import forms
from django.core.exceptions import ValidationError


# здесь продолжайте программу

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=5, required=True, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-login-input'}))
    password = forms.CharField(min_length=6, required=True, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-login-input'}))

    def clean_password(self):
        password = self.cleaned_data['password']
        valid_string = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-?!$#@_")
        if len(password) < 6 or not set(password).issubset(valid_string):
            raise ValidationError("Некорректно введенный пароль.")
        else:
            return password
