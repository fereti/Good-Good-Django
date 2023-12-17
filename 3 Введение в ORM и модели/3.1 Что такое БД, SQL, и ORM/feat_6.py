# Подвиг 6. Заполните следующий класс модели Category:
#
# class Category(models.Model):
#     # здесь прописывайте атрибуты класса
# для работы с таблицей БД следующей структуры:
#
# id: идентификатор записи (Primary Key); формируется автоматически (описывать в классе не нужно);
# name: название категории (models.CharField) с максимальной длиной 50 символов;
# time_create: время создания категории (models.DateTimeField); должно заполняться автоматически в момент создания записи
# Названия атрибутов должны совпадать с названиями полей.
#
# P.S. В программе требуется только объявить класс, создавать его объекты не нужно.


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
