# Подвиг 2. Пусть имеется следующая функция представления:
#
# def index(request):
#     data = {
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'subject/index.html', context=data)
# Замените эту функцию аналогичным классом представления с именем MainPage, унаследованным от базового класса TemplateView.
#
# В описании класса используйте только нужные атрибуты. Методы объявлять не нужно.
#
# P.S. На экран ничего выводить не нужно.


from django.views.generic import TemplateView

class MainPage(TemplateView):
    template_name = 'subject/index.html'
    extra_context = {
        'title': 'Главная страница',
        'cat_selected': 0,
    }
