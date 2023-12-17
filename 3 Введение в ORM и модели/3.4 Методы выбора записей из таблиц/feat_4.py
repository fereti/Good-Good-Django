# Подвиг 4. Объявите класс модели с именем Auto для работы с таблицей следующей структуры:
#
# id: primary key (в модели не прописывается)
# name: CharField - строка с максимальной длиной 100 символов; обязательное поле;
# model: CharField - марка машины; обязательное поле;
# price: IntegerField - цена машины с начальным значением 0; необязательное поле;
# is_exists: BooleanField - наличие товара (True - присутствует; False - отсутствует); по умолчанию True.
#
# С помощью класса Auto добавьте в БД следующие машины в порядке их перечисления:
#
# name="BMW X6"; model="BMW"; price=6000111;
# name="Toyota Corolla"; model="Toyota";
# name="Haval 7"; model="Haval"; price=3500222;
#
# Используя метод all() стандартного менеджера записей класса Auto выберите первую запись из соответствующей таблицы БД. Результат сохраните в переменной autos.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField()
    price = models.IntegerField(default=0, null=True, blank=True)
    is_exists = models.BooleanField(default=True)


Auto.objects.create(name="BMW X6", model="BMW", price=6000111)
Auto.objects.create(name="Toyota Corolla", model="Toyota")
Auto.objects.create(name="Haval 7", model="Haval", price=3500222)

autos = Auto.objects.all()[0]
