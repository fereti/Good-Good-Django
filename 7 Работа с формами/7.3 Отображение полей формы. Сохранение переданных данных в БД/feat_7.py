# Подвиг 7 (на повторение). Пусть имеется следующий класс формы:
#
# # --------------- forms.py -------------------------
# from django import forms
#
# class LectorForm(forms.Form):
#     first_name = forms.CharField(max_length=100, label="Имя")
#     last_name = forms.CharField(max_length=100, label="Фамилия")
#     email = forms.EmailField(label="E-mail")
#     salary = forms.IntegerField(required=False, label="Зарплата")
#
# # --------------- views.py -------------------------
# # from django.shortcuts import render
# # from .forms import LectorForm
#
# # здесь продолжайте программу
# Объявите функцию представления с именем lector_add, в которой:
#
# при POST-запросе формируется заполненная форма LectorForm; выполняется проверка корректности данных формы; если данные корректны, то возвращается объект формы;
# при GET-запросе создается пустая форма LectorForm; с помощью функции render формируется HTML-документ по шаблону 'lector/addlector.html' с передачей в него объекта формы LectorForm через переменную (ключ) form.
# P.S. На экран ничего выводить не нужно.


# --------------- forms.py -------------------------
from django import forms


class LectorForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="Имя")
    last_name = forms.CharField(max_length=100, label="Фамилия")
    email = forms.EmailField(label="E-mail")
    salary = forms.IntegerField(required=False, label="Зарплата")


# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import LectorForm

def lector_add(request):
    if request.method == "POST":
        form = LectorForm(request.POST)
        if form.is_valid():
            return form
    else:
        form = LectorForm()
        return render(request, 'lector/addlector.html', {'form': form})
