# Подвиг 3. Пусть имеется следующий шаблон для загрузки файлов на сервер и фрагмент программы:
#
# # --------------- templates/studio/upload_file.html --------------
#
# <form action="" method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <p><button type="submit">Загрузить документ</button></p>
# </form>
#
# # --------------- forms.py ---------------------------------------
#
# from django import forms
#
# # здесь определяйте класс формы
#
# # --------------- views.py ---------------------------------------
# # from django.shortcuts import render
# # from .forms import UploadCustomFile
#
# def handle_uploaded_file(upload):
#     """Функция-заглушка для тестирования загрузки файла"""
#     return upload
#
#
# # здесь определяйте функцию представления
# Необходимо в файле (разделе) forms.py объявить класс формы UploadCustomFile, не связанной с моделью для выбора файлов. Этот класс должен содержать одно поле:
#
# upload_file: класс FileField, обязательное, название "Выберите файл".
#
# Затем, в файле (разделе) views.py объявить функцию представления upload_custom_file со следующим функционалом:
#
# при GET-запросе должна создаваться пустая форма UploadCustomFile и с помощью функции render формироваться HTML-документ по шаблону 'studio/upload_file.html' с передачей в него объекта формы UploadCustomFile через переменную (ключ) form;
# при POST-запросе должна формироваться заполненная форма UploadCustomFile, затем, выполняться проверка корректности переданных данных методом is_valid и при успешной проверке сохраняться файл путем вызова метода handle_uploaded_file(form.cleaned_data['upload_file']);
# функция upload_custom_file и для GET и для POST запросов должна с помощью функции render возвращать HTML-документ по шаблону 'studio/upload_file.html' с передачей в него сформированного объекта формы UploadCustomFile через переменную (ключ) form.
# P.S. На экран ничего выводить не нужно.


# --------------- templates/studio/upload_file.html --------------

# <form action="" method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <p><button type="submit">Загрузить документ</button></p>
# </form>

# --------------- forms.py ---------------------------------------

from django import forms


class UploadCustomFile(forms.Form):
    upload_file = forms.FileField(required=True, label='Выберите файл')


# --------------- views.py ---------------------------------------
# from django.shortcuts import render, redirect
# from .forms import UploadCustomFile

def handle_uploaded_file(upload):
    """Функция-заглушка для тестирования загрузки файла"""
    return upload


def upload_custom_file(request):
    if request.method == 'GET':
        form = UploadCustomFile()
        return render(request, 'studio/upload_file.html', {'form': form})
    elif request.method == 'POST':
        form = UploadCustomFile(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['upload_file'])
            return render(request, 'studio/upload_file.html', {'form': form})
