# Подвиг 3. Запишите функцию представления с именем about, которая бы возвращала клиенту HTTP-ответ со строкой "О сайте".
# P. S. Функцию вызывать не нужно, только объявить.

from django.http import HttpResponse, HttpRequest


def about(request):
    return HttpResponse('О сайте')
