#  Подвиг 5. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import Count, Sum, Avg, Max, Min
#
# class Person(models.Model):
#     full_name = models.CharField(max_length=255)
#     salary = models.PositiveIntegerField(default=0)
#     age = models.PositiveIntegerField(default=0)
#     job = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#
#
# result = # здесь прописывайте команду
# Используя стандартный менеджер записей (objects) модели Person, вычислите максимальную и минимальную зарплату (salary) для каждой профессии (job) при условии, что возраст сотрудника (age) больше 30. Значения максимальной и минимальной зарплаты должно храниться в полях с именами salary_max и salary_min.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = Person.objects.values("job").filter(age__gt=30).annotate(salary_max=Max("salary"), salary_min=Min("salary"))
