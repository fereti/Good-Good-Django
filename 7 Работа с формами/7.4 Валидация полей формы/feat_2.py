# Подвиг 2. Объявите класс формы с именем CardForm, не связанной с моделью, со следующими полями:
#
# fio: текстовое поле; максимальная длина 200 символов, минимальная длина 10 символов, обязательное, название "Владелец";
# email: поле ввода адреса электронной почты; минимальная длина 5 символов, обязательное, название "E-mail";
# city: текстовое поле; минимальная длина 2 символа, обязательное, название "Город";
# is_rf: булево поле (checkbox); по умолчанию True, обязательное, название "Гражданство РФ".
#
# Атрибуты класса должны иметь те же названия и порядок, что и в описании. То есть: fio, email, city и т.д.
#
# Для поля fio дополнительно пропишите вывод сообщений об ошибках для валидаторов:
#
# превышения числа символов: "Слишком длинная строка";
# недостаточного числа символов: "Слишком короткая строка".
# Для поля email через параметр widget укажите стили оформления: attrs={'class': 'form-input'}
#
# P.S. На экран ничего выводить не нужно.


from django import forms


class CardForm(forms.Form):
    fio = forms.CharField(max_length=200, min_length=10, required=True, label='Владелец', error_messages={
        'max_length': 'Слишком длинная строка',
        'min_length': 'Слишком короткая строка',
    })
    email = forms.EmailField(min_length=5, required=True, label='E-mail',
                             widget=forms.TextInput(attrs={'class': 'form-input'}))
    city = forms.CharField(min_length=2, required=True, label='Город')
    is_rf = forms.BooleanField(initial=True, required=True, label='Гражданство РФ')
