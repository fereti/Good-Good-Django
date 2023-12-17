# Подвиг 2. Объявите класс модели Profile со следующими атрибутами:
#
# full_name: текстовое поле, максимальное число символов 200, обязательное, название "Имя";
# email: поле хранения E-mail-адреса, необязательное, название "E-mail";
# photo: поле хранения загружаемого изображения, необязательное, подкаталог загрузки "profile", название "Аватар".
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


# здесь объявляйте класс модели
class Profile(models.Model):
    full_name = models.CharField(max_length=200, blank=False, verbose_name='Имя')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    photo = models.ImageField(blank=True, upload_to='profile', verbose_name='Аватар')
