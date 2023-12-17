# Подвиг 6. Пусть в программе объявлена следующая модель:
#
# from django.db import models
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
# records = # здесь прописывайте команду
# Используя стандартный менеджер записей (objects) модели Person, выберите все записи так, чтобы в выборке фигурировали только поля full_name и salary.
#
# P.S. Порядок полей должен быть, как указано в описании. На экран ничего выводить не нужно.


from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.values("full_name", "salary")
