# Подвиг 3. Объявите класс формы с именем ContactForm, не связанной с моделью, со следующими полями:
#
# fio: текстовое поле; максимальная длина 200 символов, обязательное;
# email: поле ввода адреса электронной почты; обязательное;
# city: текстовое поле; максимальная длина 100 символов, необязательное;
# phone: текстовое поле; максимальная длина 12 символов, необязательное;
# agree: поле BooleanField; необязательное;
# content: поле ввода полноценного многострочного текста; обязательное.
#
# Атрибуты класса должны иметь те же названия и порядок, что и в описании. То есть: fio, email, city и т.д.
#
# P.S. На экран ничего выводить не нужно.


from django import forms


class ContactForm(forms.Form):
    fio = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    city = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=12, required=False)
    agree = forms.BooleanField(required=False)
    content = forms.CharField(widget=forms.Textarea(), required=True)
