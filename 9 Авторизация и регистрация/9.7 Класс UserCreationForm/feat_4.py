# Подвиг 4. Пусть имеется следующий фрагмент программы:
#
# # ---------------- forms.py -------------------------
# from django import forms
# # from django.contrib.auth import get_user_model
# # from django.contrib.auth.forms import UserCreationForm
#
# class LectorRegisterForm(UserCreationForm):
#     username = forms.CharField(max_length=50, label="Логин")
#     password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)
#
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'password1', 'password2']
#
# # ---------------- views.py -------------------------
# # from .forms import LectorRegisterForm
#
# def register(request):
#     if request.method == "POST":
#         form = LectorRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1'])
#             user.save()
#             return render(request, 'users/register_done.html')
#     else:
#         form = LectorRegisterForm()
#     return render(request, 'users/register.html', {'form': form})
# Замените функцию представления register эквивалентным классом представления с именем UserRegister, унаследованный от базового класса CreateView, со следующим функционалом:
#
# через атрибуты класса:
#
# класс формы: LectorRegisterForm;
# шаблон: 'users/register.html';
# дополнительные переменные для шаблона: {'title': "Регистрация"};
# перенаправление после успешной регистрации: reverse_lazy('users:login').


# ---------------- forms.py -------------------------
from django import forms


# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

class LectorRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="Логин")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


# ---------------- views.py -------------------------
# from .forms import LectorRegisterForm
# from django.urls import reverse_lazy

class UserRegister(CreateView):
    form_class = LectorRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Регистрация'}
