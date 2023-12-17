# Подвиг 4. Пусть имеется следующая функция представления:
#
# # from django.contrib.auth.decorators import login_required, permission_required
# # from .forms import AddPostForm
#
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             return True
#     else:
#         form = AddPostForm()
#
#     return render(request, 'women/addpage.html', {'title': 'Добавление статьи', 'form': form})
# Примените к ней декоратор permission_required так, чтобы доступ имели только пользователи с разрешением вида 'women.add_post'. Для всех других пользователей должно генерироваться исключение с кодом 403 - доступ запрещен.


from django.contrib.auth.decorators import permission_required


# from .forms import AddPostForm


@permission_required(perm='women.add_post', raise_exception=True)
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            return True
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {'title': 'Добавление статьи', 'form': form})
