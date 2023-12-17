# Подвиг 4. Объявите новую модель пользователя с именем Student с базовым классом AbstractUser и следующими дополнительными полями:
#
# photo: поле изображения (ImageField); путь для загрузки "avatars/<текущий год>/<текущий день>/", обязательное, по умолчанию "avatars/default.jpg", название "Фотография";
# group: текстовое поле; максимальная длина 100 символов, необязательное, название "Группа";
# stipend: целочисленное поле (PositiveIntegerField); необязательное, по умолчанию значение 0, название "Стипендия".
# Объявите переменную AUTH_USER_MODEL и присвойте ей значение новой модели пользователя Student приложения students.
#
# Зарегистрируйте модель Student в админ-панели, используя стандартный класс UserAdmin и декоратор admin.site.register.


# from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(AbstractUser):
    photo = models.ImageField(upload_to='avatars/%Y/%d/', blank=False, default='avatars/default.jpg',
                              verbose_name='Фотография')
    group = models.CharField(max_length=100, blank=True, verbose_name='Группа')
    stipend = models.PositiveIntegerField(blank=True, default=0, verbose_name='Стипендия')


AUTH_USER_MODEL = 'students.Student'

from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
# from .models import Student

admin.site.register(Student, UserAdmin)
