# Подвиг 5. Пусть в программе объявлена следующая модель:
#
# from django.db import models
# from django.db.models import Count, Sum, Avg, Max, Min, Q
#
# class Subject(models.Model):
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     name = models.CharField(max_length=255)
#     volume = models.PositiveIntegerField(default=16)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#
#
# result = # здесь прописывайте команду
# Используя стандартный менеджер записей (objects) модели Subject, методы filter() и aggregate(), выберите записи с price >= 2000 или volume > 16, вычислите их общее количество, а также разность между максимальным и минимальным объемами (volume). На выходе должен формироваться словарь с ключами: 'total', 'volume_diff' и соответствующими значениями. Агрегирующая функция Count() должна применяться к полю id.
#
# P.S. Порядок критериев выбора записей и вызова агрегирующих функций, как указано в описании. На экран ничего выводить не нужно.


from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min, Q


class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = Subject.objects.filter(Q(price__gte=2000) | Q(volume__gt=16)).aggregate(total=Count("id"), volume_diff=Max("volume")-Min("volume"))
