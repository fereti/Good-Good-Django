#  Подвиг 7. Пусть в программе объявлена следующая модель:
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
# Используя стандартный менеджер записей (objects) модели Person, методы filter() и values(), выберите все записи с полем job = 'python' и так, чтобы в выборке фигурировали только поля full_name, salary и age.
#
# P.S. Порядок полей должен быть, как указано в описании. На экран ничего выводить не нужно.



from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.filter(job='python').values('full_name', 'salary', 'age')
