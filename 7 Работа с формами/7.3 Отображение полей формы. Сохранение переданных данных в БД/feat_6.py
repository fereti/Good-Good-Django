# Подвиг 6. Пусть имеется следующий класс формы:
#
# class ContactForm(forms.Form):
#     fio = forms.CharField(max_length=200)
#     email = forms.EmailField()
#     city = forms.CharField(max_length=100, required=False)
#     phone = forms.CharField(max_length=12, required=False)
#     agree = forms.BooleanField(initial=False, required=False)
#     content = forms.CharField(widget=forms.Textarea())
# Дополните его следующей информацией:
#
# заголовки полей: fio - "ФИО"; email - "E-mail"; city - "Город"; phone - "Телефон"; agree - "Согласие на обработку"; content - "Сообщение";
# полям fio, email, city, phone назначить стиль оформления attrs={'class': 'form-input'};
# поле content установить шириной (cols) 30 единиц, высотой (rows) 7 единиц.


from django import forms


class ContactForm(forms.Form):
    fio = forms.CharField(max_length=200, label='ФИО', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
    city = forms.CharField(max_length=100, required=False, label='Город',
                           widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = forms.CharField(max_length=12, required=False, label='Телефон',
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    agree = forms.BooleanField(initial=False, required=False, label='Согласие на обработку')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 7}), label='Сообщение')
