# Подвиг 5. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=False)
#
# # --------- views.py ------------------------
# # from django.shortcuts import get_object_or_404
# # from .models import Post
#
# def show_post(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug, is_published=1)
#
#     data = {
#         'title': post.title,
#         'post': post,
#     }
#
#     return render(request, 'post/detail_post.html', data)
# Замените эту функцию классом представления с именем PostDetail, унаследованным от базового класса DetailView, со следующим функционалом:
#
# через атрибуты класса:
#
# используемый шаблон: 'post/detail_post.html';
# имя переменной для шаблона с объектом записи: post;
# через методы класса:
#
# get_object: извлечение записи по критерию: slug = post_slug и is_published = 1; для получения записи использовать функцию get_object_or_404();
# get_context_data: сформировать следующие переменные для шаблона: {'title': "Заголовок поста", 'cat_selected': 0}.
# P.S. На экран ничего выводить не нужно.


# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


# --------- views.py ------------------------
from django.views.generic import DetailView


# from django.shortcuts import get_object_or_404
# from .models import Post

class PostDetail(DetailView):
    template_name = 'post/detail_post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs[self.slug_url_kwarg], is_published=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заголовок поста'
        context['cat_selected'] = 0
        return context
