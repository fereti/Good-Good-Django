# Подвиг 5. Пусть имеется следующий класс модели:
#
# from django.db import models
#
# class CourseItem(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
# Необходимо с помощью метода get() стандартного менеджера записей класса CourseItem извлечь запись с pk равным 2 и сохранить объект в переменной item. Затем, изменить в объекте item следующие поля:
#
# title="Python ООП"
# content="Обучающий курс по Python ООП"
#
# После этого изменить в таблице БД запись объекта item.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


item = CourseItem.objects.get(pk=2)
item.title = "Python ООП"
item.content = "Обучающий курс по Python ООП"
item.save()
