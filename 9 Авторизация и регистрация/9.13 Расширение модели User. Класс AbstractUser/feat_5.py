# Подвиг 5. Выполните расширение стандартной модели User с использованием связи one-to-one. Для этого объявите класс модели с именем Profile со следующими атрибутами:
#
# user: связь one-to-one со стандартной моделью User (пропишите класс User в кавычках в виде строки); удаление связанных записей по алгоритму CASCADE;
# photo: поле изображения (ImageField); путь для загрузки "users/<текущий год>/<текущий месяц>/", необязательное, по умолчанию "users/default.jpg", название "Изображение";
# date_birth: поле с датой (DateField); необязательное, допустимо значение NULL, название "Дата рождения".
# Зарегистрируйте для админ-панели модель Profile. Во вспомогательном классе ProfileAdmin (унаследованный от admin.ModelAdmin) определите следующие атрибуты:
#
# отображаемые поля: user, photo, date_birth;
# редактируемые поля: date_birth;
# поля при редактировании записи: user, photo, date_birth.
# P.S. На экран ничего выводить не нужно.


# from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/', blank=True, default='users/default.jpg',
                              verbose_name='Изображение')
    date_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')


from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'date_birth')
    list_editable = ['date_birth']
    fields = ('user', 'photo', 'date_birth')


admin.site.register(Profile)
