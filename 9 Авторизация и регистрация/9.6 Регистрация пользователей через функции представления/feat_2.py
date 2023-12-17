# Подвиг 2. Объявите класс формы LectorRegisterForm для регистрации преподавателей. Форма LectorRegisterForm должна быть связана с моделью User, доступ к которой следует выполнить с помощью функции get_user_model(). Сама же форма должна иметь следующие элементы:
#
# через атрибуты класса:
#
# username: текстовое поле, максимальная длина 50 символов, название "Логин";
# password: поле ввода пароля, максимальная длина 30 символов, название "Пароль";
# password2: поле ввода пароля, максимальная длина 30 символов, название "Повтор пароля";
# через атрибуты вложенного класса Meta:
#
# модель: определяется вызовом функции get_user_model();
# отображаемые в форме поля: username, email, password, password2;
# дополнительные метки (названия) полей: email -> "E-mail".
# P.S. На экран ничего выводить не нужно.


from django import forms


class LectorRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин', max_length=50)
    password = forms.CharField(label='Пароль', max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']
        labels = {
            'email': 'E-mail',
        }
