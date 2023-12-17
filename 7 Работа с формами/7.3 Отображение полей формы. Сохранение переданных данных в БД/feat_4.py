# Подвиг 4. Объявите класс формы с именем OsagoForm, не связанной с моделью, со следующими полями:
#
# fio: текстовое поле; максимальная длина 200 символов, обязательное, название "Владелец";
# email: поле ввода адреса электронной почты; обязательное, название "E-mail";
# vin: текстовое поле; максимальная длина 20 символов, обязательное, название "VIN";
# model: текстовое поле; максимальная длина 100 символов, обязательное, название "Модель";
# stag: числовое поле; необязательное, название "Стаж".
#
# Атрибуты класса должны иметь те же названия и порядок, что и в описании. То есть: fio, email, vin  и т.д.
#
# P.S. На экран ничего выводить не нужно.


from django import forms


class OsagoForm(forms.Form):
    fio = forms.CharField(max_length=200, label='Владелец')
    email = forms.EmailField(required=True, label='E-mail')
    vin = forms.CharField(max_length=20, required=True, label='VIN')
    model = forms.CharField(max_length=100, required=True, label='Модель')
    stag = forms.IntegerField(required=False, label='Стаж')
