# Подвиг 4. Пусть имеется следующий класс формы:
#
# # --------------- forms.py -------------------------
# from django import forms
#
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     slug = forms.SlugField(max_length=255)
#     content = forms.CharField(widget=forms.Textarea(), required=False)
#     is_published = forms.BooleanField(required=False)
#
# # --------------- views.py -------------------------
# # from django.shortcuts import render
# # from .forms import AddPostForm
#
# # здесь продолжайте программу
# Объявите функцию представления с именем post_new, в которой:
#
# создается пустая форма AddPostForm;
# с помощью функции render формируется HTML-документ по шаблону 'women/addpage.html' с передачей в него объекта формы AddPostForm через переменную (ключ) form.
# P.S. На экран ничего выводить не нужно.


# --------------- forms.py -------------------------
from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)


# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import AddPostForm

def post_new(request):
    form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form})
