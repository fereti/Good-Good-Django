# Подвиг 4. Пусть имеется следующий шаблон для загрузки файлов на сервер и фрагмент программы:
#
# # --------------- templates/studio/upload_file.html --------------
#
# <form action="" method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <p><button type="submit">Загрузить изображение</button></p>
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
# # from .forms import UploadImageFile
#
# def handle_uploaded_image(upload):
#     """Функция-заглушка для тестирования загрузки файла"""
#     return upload
#
#
# # здесь определяйте функцию представления
# Необходимо в файле (разделе) forms.py объявить класс формы UploadImageFile, не связанной с моделью для выбора файлов. Этот класс должен содержать одно поле:
#
# upload_image: класс ImageField, обязательное, название "Выберите изображение".
#
# Затем, в файле (разделе) views.py объявить функцию представления upload_image_file со следующим функционалом:
#
# при GET-запросе должна создаваться пустая форма UploadImageFile и с помощью функции render формироваться HTML-документ по шаблону 'studio/upload_file.html' с передачей в него объекта формы UploadImageFile через переменную (ключ) form;
# при POST-запросе должна формироваться заполненная форма UploadImageFile, затем, выполняться проверка корректности переданных данных методом is_valid и при успешной проверке сохраняться файл путем вызова метода handle_uploaded_image(form.cleaned_data['upload_image']);
# функция upload_image_file и для GET и для POST запросов должна с помощью функции render возвращать HTML-документ по шаблону 'studio/upload_file.html' с передачей в него сформированного объекта формы UploadImageFile через переменную (ключ) form.
# P.S. На экран ничего выводить не нужно.


# --------------- templates/studio/upload_file.html --------------

# <form action="" method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <p><button type="submit">Загрузить изображение</button></p>
# </form>

# --------------- forms.py ---------------------------------------

from django import forms


class UploadImageFile(forms.Form):
    upload_image = forms.ImageField(required=True, label='Выберите изображение')


# --------------- views.py ---------------------------------------
# from django.shortcuts import render
# from .forms import UploadImageFile

def handle_uploaded_image(upload):
    """Функция-заглушка для тестирования загрузки файла"""
    return upload


def upload_image_file(request):
    if request.method == 'GET':
        form = UploadImageFile()
        return render(request, 'studio/upload_file.html', {'form': form})
    elif request.method == 'POST':
        form = UploadImageFile(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_image(request.FILES['upload_image'])
            return render(request, 'studio/upload_file.html', {'form': form})
