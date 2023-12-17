# Подвиг 3. Пусть имеется следующая функция представления для авторизации пользователей:
#
# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginUserForm()
#     return render(request, 'profile/login.html', {'form': form})
# Необходимо ее заменить классом представления LoginProfile, унаследованным от базового класса LoginView, со следующим функционалом:
#
# через атрибуты класса:
#
# форма для авторизации: AuthenticationForm;
# шаблон для отображения формы: 'profile/login.html';
# дополнительные параметры: {'title': "Авторизация"};
# через методы класса:
#
# перенаправление при успешной авторизации по маршруту с именем 'home', используя функцию reverse_lazy.
# P.S. На экран ничего выводить не нужно.


# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy

class LoginProfile(LoginView):
    form_class = AuthenticationForm
    template_name = 'profile/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')
