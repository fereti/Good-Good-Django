# Подвиг 4. Объявите класс представления LectorPasswordChange с базовым классом PasswordChangeView и следующими характеристиками:
#
# через атрибуты класса:
#
# класс формы: LectorPasswordChangeForm;
# шаблон: "lector/password_change_form.html";
# перенаправление при успешном изменении пароля: reverse_lazy("password_change_done");
# дополнительные переменные для шаблона: {'title': "Изменение пароля"}.
# P.S. На экран ничего выводить не нужно.


class LectorPasswordChange(PasswordChangeView):
    form_class = LectorPasswordChangeForm
    template_name = 'lector/password_change_form.html'
    success_url = reverse_lazy("password_change_done")
    extra_context = {'title': "Изменение пароля"}
