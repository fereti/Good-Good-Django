# Подвиг 4. Пусть имеется следующая функция представления:
#
# def show_post(request, post_slug):
#     # заглушка вместо вызова get_object_or_404(Women, slug=post_slug)
#     post = {'title': 'Заголовок', 'slug': post-slug, 'content': 'Супер пост'}
#
#     data = {
#         'title': post['title'],
#         'post': post,
#         'cat_selected': 0,
#     }
#
#     return render(request, 'post/post_detail.html', context=data)
# Замените эту функцию аналогичным классом представления с именем PostDetail, унаследованным от базового класса TemplateView. Класс должен иметь следующее содержимое:
#
# атрибут для использования шаблона 'post/post_detail.html';
# метод get_context_data для передачи в шаблон данных из словаря data.
# Вместо функции get_object_or_404() используйте словарь:
#
# post = {'title': 'Заголовок', 'slug': 'post-slug', 'content': 'Супер пост'}
# P.S. На экран ничего выводить не нужно.


from django.views.generic import TemplateView


class PostDetail(TemplateView):
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = {'title': 'Заголовок', 'slug': 'post-slug', 'content': 'Супер пост'}
        context['title'] = post['title']
        context['post'] = post
        context['cat_selected'] = 0
        return context
