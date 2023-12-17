# Подвиг 4. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     is_published = models.BooleanField(default=True)
#
# # --------- views.py ------------------------
# from django.views.generic import ListView
# # from .models import Post
#
# def post_list(request):
#     data = {
#         'title': 'Список статей',
#         'p_list': Post.objects.filter(is_published=1),
#     }
#
#     return render(request, 'post/listpost.html', context=data)
# Замените функцию post_list эквивалентным классом представления PostList, унаследованным от базового класса ListView, со следующим функционалом:
#
# через атрибуты класса:
#
# шаблон: 'post/listpost.html';
# переменная со списком записей (в шаблоне): p_list;
# дополнительные переменные: {'title': 'Список статей'};
# пагинация: разбиение по 3 записи на страницу;
# через методы класса:
#
# get_queryset: выборка записей через модель Post с полем is_published=1 (используя стандартный менеджер записей модели).
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)


# --------- views.py ------------------------
from django.views.generic import ListView


# from .models import Post

class PostList(ListView):
    template_name = 'post/listpost.html'
    context_object_name = 'p_list'
    paginate_by = 3
    extra_context = {
        'title': 'Список статей'
    }

    def get_queryset(self):
        return Post.objects.filter(is_published=1)
