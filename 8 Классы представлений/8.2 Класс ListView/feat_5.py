# Подвиг 5. Пусть имеется следующий фрагмент программы:
#
# # --------- models.py ------------------------
# from django.db import models
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, blank=True, db_index=True)
#
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
#
#
# # --------- views.py ------------------------
# from django.views.generic import ListView
# # from .models import Post
#
# # здесь объявляйте класс PostListCategory
#
#
# # --------- urls.py ------------------------
#
# from django.urls import path
# # from .views import PostListCategory
#
# urlpatterns = [
#     path('category/<slug:cat_slug>/', PostListCategory.as_view(), name='category'),
# ]
# Объявите класс представления PostListCategory в разделе views.py, унаследованного от класса ListView, со следующим функционалом:
#
# через атрибуты класса:
#
# шаблон для отображения статей: 'post/list.html';
# переменная со списком выбранных записей из модели Post (для передачи в шаблон): cat_posts;
# запрет на отображение страницы без записей (должно генерироваться исключение 404);
# через методы класса:
#
# метод формирования (для шаблона) переменной title со значением "Список постов по рубрике";
# метод для выборки записей: с помощью стандартного менеджера записей модели Post и метода filter выбрать все посты, у которых поле slug модели Category равно параметру cat_slug URL-маршрута.
# P.S. На экран ничего выводить не нужно


# --------- models.py ------------------------
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')


# --------- views.py ------------------------
from django.views.generic import ListView


# from .models import Post

class PostListCategory(ListView):
    template_name = 'post/list.html'
    context_object_name = 'cat_posts'
    allow_empty = False

    def get_queryset(self):
        cat_slug = self.kwargs['cat_slug']
        queryset = Post.objects.filter(cat__slug=cat_slug)
        if not queryset:
            raise Http404
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список постов по рубрике'
        return context

    # --------- urls.py ------------------------


from django.urls import path

# from .views import PostListCategory

urlpatterns = [
    path('category/<slug:cat_slug>/', PostListCategory.as_view(), name='category'),
]
