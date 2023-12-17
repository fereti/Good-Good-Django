# Подвиг 3. Пусть имеется следующий фрагмент программы:
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
# # --------- forms.py ------------------------
# from django import forms
# # from .models import Post
#
# class AddPostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'slug', 'content']
#
# # --------- views.py ------------------------
# # from django.shortcuts import render, redirect
# # from .forms import AddPostForm
#
# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = AddPostForm()
#
#     return render(request, 'post/addpost.html', {'title': 'Добавление статьи', 'form': form})
# Замените функцию add_post аналогичным классом представления с именем AddPost, унаследованным от базового класса View.
#
# В классе AddPost должны быть объявлены только два метода get и post с соответствующим содержимым.
#
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


# --------- forms.py ------------------------
from django import forms


# from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']


# --------- views.py ------------------------
from django.views import View


# from django.shortcuts import render, redirect
# from .forms import AddPostForm

class AddPost(View):
    def get(self, request):
        form = AddPostForm()
        return render(request, 'post/addpost.html', {'title': 'Добавление статьи', 'form': form})

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

        return render(request, 'post/addpost.html', {'title': 'Добавление статьи', 'form': form})
