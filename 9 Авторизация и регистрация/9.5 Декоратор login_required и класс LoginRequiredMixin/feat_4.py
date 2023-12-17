# Подвиг 4. Пусть имеется следующий класс представления:
#
# from django.contrib.auth.mixins import LoginRequiredMixin
#
# class ListPost(ListView):
#     template_name = 'post/list.html'
#     model = Post
#     context_object_name = 'posts'
#     extra_context = {
#         'title': 'Список опубликованных статей',
#     }
# Примените к нему класс LoginRequiredMixin, чтобы ограничить доступ неавторизованным пользователям.


# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class ListPost(LoginRequiredMixin, ListView):
    template_name = 'post/list.html'
    model = Post
    context_object_name = 'posts'
    extra_context = {
        'title': 'Список опубликованных статей',
    }
