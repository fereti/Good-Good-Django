# Подвиг 3. Пусть имеется следующий класс представления:
#
# # from .models import Person
# # from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.views.generic import ListView
#
# class PersonList(ListView):
#     model = Person
#     template_name = 'person/list.html'
#     context_object_name = 'persons'
#     allow_empty = False
#     paginate_by = 3
# Отредактируйте этот класс, разрешив просмотр списка только пользователям с разрешением вида 'users.view_person'.


# from .models import Person
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView


class PersonList(PermissionRequiredMixin, ListView):
    model = Person
    permission_required = 'users.view_person'
    template_name = 'person/list.html'
    context_object_name = 'persons'
    allow_empty = False
    paginate_by = 3
