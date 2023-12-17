# Подвиг 3. Объявите класс формы ProfilePasswordChangeForm для смены пароля с базовым классом PasswordChangeForm и следующими характеристиками:
#
# через атрибуты класса:
#
# старый пароль: текстовое поле, название "Старый пароль", CSS-стили attrs={'class': 'form-input'};
# новый пароль: поле ввода пароля, название "Новый пароль", CSS-стили attrs={'class': 'form-input'};
# повтор пароля: поле ввода пароля, название "Подтверждение пароля", CSS-стили attrs={'class': 'form-input'}.
# Атрибуты для полей ввода должны соответствовать базовой форме PasswordChangeForm.
#
# P.S. На экран ничего выводить не нужно.


# from django.contrib.auth.forms import PasswordChangeForm
from django import forms


class ProfilePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль",
                                   widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль",
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля",
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
