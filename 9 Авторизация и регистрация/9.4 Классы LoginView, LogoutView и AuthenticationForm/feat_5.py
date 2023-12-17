# Подвиг 5. На основе базового класса AuthenticationForm объявите новый класс формы с именем NewUserLoginForm со следующими элементами:
#
# через атрибуты вложенного класса Meta:
#
# модель формы: текущая модель пользователя, возвращенная функцией get_user_model();
# отображаемые поля в форме авторизации: username, password.
# P.S. На экран ничего выводить не нужно.


# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import get_user_model

class NewUserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
