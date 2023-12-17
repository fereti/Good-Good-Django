# Подвиг 5. Объявите класс представления CompanyPasswordChangeDone с базовым классом PasswordChangeDoneView и следующими характеристиками:
#
# через атрибуты класса:
#
# шаблон отображения: "company/password_change_done.html";
# дополнительные переменные для шаблона: {'title': "Пароль изменен"}.
# P.S. На экран ничего выводить не нужно.


# from django.contrib.auth.views import PasswordChangeDoneView


class CompanyPasswordChangeDone(PasswordChangeDoneView):
    template_name = "company/password_change_done.html"
    extra_context = {'title': 'Пароль изменен'}
