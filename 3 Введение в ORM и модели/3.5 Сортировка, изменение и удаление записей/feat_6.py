# Подвиг 6. Пусть имеется следующий класс модели:
#
# from django.db import models
#
# class CourseItem(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
# С помощью методов filter() и update() стандартного менеджера записей класса CourseItem у записей со значением is_published=False изменить поле content на пустую строку.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


CourseItem.objects.filter(is_published=False).update(content='')
