# Подвиг 3. Объявите класс модели с именем ShopItem для работы с таблицей следующей структуры:
#
# id: primary key (в модели не прописывается)
# name: CharField - строка с максимальной длиной 100 символов; обязательное поле;
# weight: IntegerField - вес товара с начальным значением 0; не обязательное поле;
# price: IntegerField - цена товара с начальным значением 0; обязательное поле;
# is_exists: BooleanField - наличие товара (True - присутствует; False - отсутствует); по умолчанию True.
#
# Используя метод all() стандартного менеджера записей класса ShopItem, выберите все записи из соответствующей таблицы БД и сохраните их в переменной records.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


class ShopItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование товара')
    weight = models.IntegerField(default=0, blank=True, verbose_name='Вес товара')
    price = models.IntegerField(default=0, verbose_name='Цена товара')
    is_exists = models.BooleanField(default=True, verbose_name='Наличие товара')


records = ShopItem.objects.all()
