# Подвиг 5. Пусть имеется функция представления с именем catalog. Необходимо ее связать с маршрутом так, чтобы она срабатывала на URL-адрес:
# http://127.0.0.1:8000/women/cat/
# Используйте для этого функцию path() фреймворка Django. Полагается, что коллекция urlpatterns определяется в пакете конфигурации проекта сайта.


from django.urls import path
from django.http import HttpResponse


def catalog(request):
    return HttpResponse("catalog")


urlpatterns = [
    path('women/cat/', catalog, name='catalog'),
]
