# Подвиг 3. Объявите класс модели с именем Profile для работы с таблицей следующей структуры:
#
# id: primary key (в модели не прописывается)
# first_name: CharField - строка с максимальной длиной 100 символов; не обязательное поле;
# last_name: CharField - строка с максимальной длиной 150 символов; не обязательное поле;
# birth_day: DateTimeField - дата рождения; не обязательное поле;
# is_banned: BooleanField - флаг бана профайла (True - забанен; False - активен); по умолчанию False.
# P.S. На экран ничего выводить не нужно.


from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    birth_day = models.DateTimeField(auto_now=True)
    is_banned = models.BooleanField(default=False)
