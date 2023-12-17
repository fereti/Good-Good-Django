# Подвиг 4. Объявите класс модели с именем Post следующей структуры:
#
# id: primary key (в модели явно не прописывается);
# slug: SlugField - slug поста, максимум 255 символов; уникальное, обязательное поле;
# title: CharField - строка, максимум 200 символов; обязательное поле;
# content: TextField - текст статьи; необязательное поле;
# time_create: DateTimeField - время создания записи (заполняется автоматически);
# time_update: DateTimeField - время последнего изменения записи (заполняется автоматически);
# is_published: BooleanField - флаг отображения поста (True - отображается; False - не отображается); по умолчанию False.
#
# P.S. На экран ничего выводить не нужно.


from django.db import models


# здесь объявляйте класс модели
class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
