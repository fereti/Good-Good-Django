# Подвиг 2. Объявите класс ExtraAttributeMixin, который бы в словарь extra_context добавлял следующие атрибуты дочернего класса:
#
# category_id: идентификатор выбранной категории (целое число);
# default_photo: путь к аватарке по умолчанию.
# Атрибуты добавляются в словарь extra_context как ключи (в виде строк 'category_id' или 'default_photo') с соответствующими значениями. Если какой-либо атрибут в дочернем классе не определен, то в словаре extra_context он должен отсутствовать.
#
# Пример использования класса ExtraAttributeMixin:
#
# class ShowPost(ExtraAttributeMixin, DetailView):
#     template_name = 'women/post.html'
#     category_id = 0 # в словарь extra_context добавляется ключ 'category_id' со значением 0
#     model = Women
#     pk_url_kwarg = 'post_pk'
#     context_object_name = 'post'
#     extra_context = {'title': "Содержимое поста"}


from django.views.generic import DetailView


class ExtraAttributeMixin:
    category_id = 0
    default_photo = None
    extra_context = {}

    def __init__(self):

        if self.category_id:
            self.extra_context['category_id'] = self.category_id

        if self.default_photo:
            self.extra_context['default_photo'] = self.default_photo


# from .models import Women

class ShowPost(ExtraAttributeMixin, DetailView):
    template_name = 'women/post.html'
    category_id = 0  # в словарь extra_context добавляется ключ 'category_id' со значением 0
    model = Women
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'
    extra_context = {'title': "Содержимое поста"}
