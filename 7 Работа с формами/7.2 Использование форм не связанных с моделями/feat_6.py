# Подвиг 6. Объявите класс формы с именем CommentForm, не связанной с моделью, со следующими полями:
#
# username: текстовое поле; максимальная длина 100 символов, обязательное;
# email: поле ввода адреса электронной почты; обязательное;
# agree: поле типа CheckBox; обязательное;
# content: поле ввода полноценного многострочного текста; обязательное.
#
# Атрибуты класса должны иметь те же названия и порядок, что и в описании. То есть: username, email, agree и т.д.
#
# # --------------- forms.py -------------------------
# from django import forms
#
# # здесь объявляйте класс формы
#
# # --------------- views.py -------------------------
# # from django.shortcuts import render
# # from .forms import CommentForm
#
# # здесь объявляйте функцию представления
# Объявите функцию представления с именем comment_add, в которой:
#
# при POST-запросе формируется заполненная форма CommentForm; выполняется проверка корректности данных формы; если данные корректны, то возвращается объект формы;
# при GET-запросе создается пустая форма CommentForm; с помощью функции render формируется HTML-документ по шаблону 'user/comment_add.html' с передачей в него объекта формы CommentForm через переменную (ключ) form.
# P.S. На экран ничего выводить не нужно.


# --------------- forms.py -------------------------
from django import forms


class CommentForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    agree = forms.BooleanField(required=True)
    content = forms.CharField(widget=forms.Textarea(), required=True)


# --------------- views.py -------------------------
def comment_add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        return form
    else:
        form = CommentForm()

    return render(request, 'user/comment_add.html', {'form': form})
