# Подвиг 2. Объявите класс представления ProfilePasswordChange с базовым классом PasswordChangeView и следующими характеристиками:
#
# через атрибуты класса:
#
# стандартный класс формы изменения пароля;
# шаблон: "profile/password_change_form.html";
# перенаправление при успешном изменении пароля: reverse_lazy("password_change_done");
# дополнительные переменные для шаблона: {'title': "Изменение пароля"}.
# P.S. На экран ничего выводить не нужно.


from django import forms


# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.views import PasswordChangeView


class ProfilePasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "profile/password_change_form.html"
    success_url = reverse_lazy("password_change_done")
    extra_context = {'title': "Изменение пароля"}
