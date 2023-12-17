# Подвиг 3. Пусть в программе объявлены следующие модели:
#
# # ---------------- models.py -------------------------
# from django.db import models
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#
#
# class Subject(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, db_index=True, unique=True)
#     descr = models.TextField(blank=True)
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
#
# # ---------------- forms.py -------------------------
# from django import forms
# # from .models import Subject, Category
#
# # здесь продолжайте программу
# Объявите класс формы SubjectForm, связанной с моделью Subject и следующими свойствами:
#
# отображаемые поля (с сохранением порядка): title, slug, descr, cat; прописывается во вложенном классе Meta;
# поля title и slug должны иметь CSS-стили attrs={'class': 'form-input'}; прописывается во вложенном классе Meta;
# поле descr должно иметь CSS-стили attrs={'cols': 50, 'rows': 5} и быть необязательным; прописывается в форме SubjectForm, как объект класса соответствующего поля;
# поле cat должно наполняться всеми записями из модели Category; не выбранный пункт должен называться "Выберите категорию"; прописывается в форме SubjectForm, как объект класса соответствующего поля.
# P.S. На экран ничего выводить не нужно.


# ---------------- models.py -------------------------
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


class Subject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    descr = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')


# ---------------- forms.py -------------------------
from django import forms


# from .models import Subject, Category

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'slug', 'descr', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
        }

    descr = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Выберите категорию')
