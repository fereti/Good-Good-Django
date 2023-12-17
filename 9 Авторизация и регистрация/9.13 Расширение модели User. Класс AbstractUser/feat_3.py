# Подвиг 3. Объявите новую модель пользователя с именем Lector с базовым классом AbstractUser и следующими дополнительными полями:
#
# avatar: поле изображения (ImageField); путь для загрузки "avatars/<текущий год>/<текущий месяц>/", необязательное, по умолчанию "avatars/default.jpg", название "Изображение";
# status: текстовое поле; максимальная длина 200 символов, необязательное, название "Должность";
# salary: целочисленное поле (IntegerField); необязательное, по умолчанию значение 0, название "Зарплата".
# Объявите переменную AUTH_USER_MODEL и присвойте ей значение новой модели пользователя Lector приложения users.
#
# P.S. На экран ничего выводить не нужно.


# from django.contrib.auth.models import AbstractUser
from django.db import models


class Lector(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/%Y/%m/", blank=True, null=True, default='avatarts/default.jpg',
                               verbose_name="Изображение")
    status = models.CharField(max_length=200, blank=True, verbose_name='Должность')
    salary = models.IntegerField(default=0, blank=True, verbose_name='Зарплата')


AUTH_USER_MODEL = 'users.Lector'
