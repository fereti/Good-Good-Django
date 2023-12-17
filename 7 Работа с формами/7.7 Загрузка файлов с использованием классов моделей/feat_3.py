# Подвиг 3. Пусть в программе объявлена следующая модель:
#
# # --------------- models.py ---------------------------------------
# from django.db import models
#
# class Post(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
#     title = models.CharField(max_length=255, verbose_name="Заголовок")
#     photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name="Изображение")
#     content = models.TextField(blank=True, verbose_name="Текст статьи")
#     is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
#
# # --------------- forms.py ---------------------------------------
# from django import forms
# #from .models import Post
#
# # здесь продолжайте программу
# Необходимо объявить класс формы PostForm, связанной с моделью Post, со следующими свойствами, прописанными во вложенном классе Meta:
#
# отображаемые поля: title, slug, photo, content;
# CSS-стили attrs={'class': 'form-input'} для полей title, slug;
# CSS-стили attrs={'cols': 50, 'rows': 5} для поля content.
# P.S. На экран ничего выводить не нужно.


# --------------- models.py ---------------------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name="Изображение")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")


# --------------- forms.py ---------------------------------------
from django import forms


# from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'photo', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
