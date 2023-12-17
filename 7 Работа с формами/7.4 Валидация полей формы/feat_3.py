# Подвиг 3. В программе импортированы следующие два валидатора:
#
# from django import forms
# from django.core.validators import MinValueValidator, MaxValueValidator
#
# # здесь продолжайте программу
# Определите целочисленное поле формы с ограничениями по диапазону вводимых данных от -100 до 20 включительно (через параметры min_value и max_value). Эти ограничения должны действовать и на уровне формы в браузере и на уровне сервера при ее обработке. Также добавьте валидаторы MinValueValidator и MaxValueValidator. В каждом из них определите следующие сообщения об ошибках:
#
# MinValueValidator: "Минимальное значение -100";
# MaxValueValidator: "Максимальное значение 20".
# На объект созданного целочисленного поля должна ссылаться переменная с именем field.
#
# P.S. Класс формы объявлять не нужно, только переменную с именем field. На экран ничего выводить не нужно.


from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

field = forms.IntegerField(min_value=-100, max_value=20,
                           validators=[MinValueValidator(-100, message="Минимальное значение -100"),
                                       MaxValueValidator(20, message="Максимальное значение 20")])
