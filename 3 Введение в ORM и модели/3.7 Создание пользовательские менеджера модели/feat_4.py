# Подвиг 4. Используя базовый класс TextChoices:
#
# from django.db.models import TextChoices
# объявите класс перечисления с именем Currencies для следующих валют (порядок следования важен):
#
# Атрибут класса; значение; метка
# RUB; 'rub'; 'Рубли'
# EUR; 'eur'; 'Евро'
# USD; 'usd'; 'Доллар'
#
# # P.S. На экран ничего выводить не нужно.


from django.db.models import TextChoices


class Currencies(TextChoices):
    RUB = 'rub', 'Рубли'
    EUR = 'eur', 'Евро'
    USD = 'usd', 'Доллар'
