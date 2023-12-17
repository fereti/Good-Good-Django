# Подвиг 5. Пусть имеется следующий класс представления:
#
# # from django.contrib.auth.mixins import LoginRequiredMixin
# # from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
#
# class AddPerson(CreateView):
#     form_class = PersonForm
#     template_name = 'person/person_create.html'
#     success_url = reverse_lazy('list-person')
#     extra_context = {'title': 'Новая персона'}
# Примените к нему класс LoginRequiredMixin, чтобы ограничить доступ неавторизованным пользователям. При попытке получить доступ неавторизованным пользователем автоматически перенаправлять по URL-адресу '/home/'.


# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class AddPerson(LoginRequiredMixin, CreateView):
    form_class = PersonForm
    login_url = '/home/'
    template_name = 'person/person_create.html'
    success_url = reverse_lazy('list-person')
    extra_context = {'title': 'Новая персона'}
