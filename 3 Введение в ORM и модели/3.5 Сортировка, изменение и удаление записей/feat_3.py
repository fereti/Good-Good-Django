# Подвиг 3. Пусть имеется следующий класс модели:

# from django.db import models

# class CourseItem(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
# С помощью стандартного менеджера записей класса CourseItem выберите все записи и отсортируйте их в порядке убывания поля title.

# P.S. На экран ничего выводить не нужно.


from django.db import models


class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


CourseItem.objects.all().order_by('-title')
