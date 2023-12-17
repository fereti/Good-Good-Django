# Подвиг 3. Пусть имеется следующая функция представления:
#
# from django.contrib.auth.decorators import login_required
#
# def support(request):
#     data = {
#         'title': 'Поддержка клиентов',
#     }
#
#     return render(request, 'users/support.html', context=data)
# Примените к ней декоратор login_required, чтобы запретить просмотр неавторизованным пользователям. При попытке получить доступ неавторизованным пользователем автоматически перенаправлять по URL-адресу с именем 'login'.


from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def support(request):
    data = {
        'title': 'Поддержка клиентов',
    }

    return render(request, 'users/support.html', context=data)
