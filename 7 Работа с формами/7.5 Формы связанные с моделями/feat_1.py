# Подвиг 1. Пусть в программе объявлена следующая модель:
#
# # ---------------- models.py -------------------------
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
#
# # ---------------- forms.py -------------------------
# from django import forms
# # from .models import Post
#
# # здесь продолжайте программу
# Объявите класс формы PostForm, связанной с моделью Post, с отображением следующих полей:
#
# title, slug, is_published, content
#
# Порядок отображения полей в форме должен быть именно таким.
#
# P.S. На экран ничего выводить не нужно.


# ---------------- models.py -------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


# ---------------- forms.py -------------------------
from django import forms


# from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'is_published', 'content']
