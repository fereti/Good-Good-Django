# Подвиг 5 (на повторение). Пусть имеется следующий фрагмент программы:
#
# # --------- views.py ------------------------
# from django.views import View
# # from django.shortcuts import render
#
# class PostView(View):
#     def get(self, request):
#         return render(request, 'post/post_detail.html', {'title': 'Добавление статьи'})
#
#
# # --------- urls.py ------------------------
# from django.urls import path
# # from .views import PostView
#
# urlpatterns = [
#     # здесь прописывайте маршрут
# ]
# Необходимо в коллекции urlpatterns с помощью функции path прописать маршрут связи URL-адреса:
#
# http://127.0.0.1:8000/main/
#
# с классом представления PostView. Имя маршрута определить строкой 'mainpage'.
#
# P.S. На экран ничего выводить не нужно.


# --------- views.py ------------------------
from django.views import View


# from django.shortcuts import render

class PostView(View):
    def get(self, request):
        return render(request, 'post/post_detail.html', {'title': 'Добавление статьи'})


# --------- urls.py ------------------------
from django.urls import path

# from .views import PostView

urlpatterns = [
    path('main/', PostView.as_view(), name='mainpage')
]
