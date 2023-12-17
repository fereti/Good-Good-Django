# Подвиг 4. Пусть имеется следующая функция представления:
#
# def show_post(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#
#     data = {
#         'title': "Содержание поста",
#         'post': post,
#         'cat_selected': 0,
#     }
#
#     return render(request, 'post/detail_post.html', data)
# Замените эту функцию классом представления с именем PostDetail, унаследованным от базового класса DetailView, со следующим функционалом:
#
# через атрибуты класса:
#
# используемый шаблон: 'post/detail_post.html';
# модель: Post;
# имя переменной для шаблона с объектом записи: post;
# извлечение записи по переменной post_slug;
# дополнительные переменные для шаблона: {'title': "Содержание поста", 'cat_selected': 0}.
# P.S. На экран ничего выводить не нужно.


from django.views.generic import DetailView


# from .models import Post

class PostDetail(DetailView):
    model = Post
    template_name = 'post/detail_post.html'
    context_object_name = 'post'
    extra_context = {
        'title': 'Содержание поста',
        'cat_selected': 0
    }
    slug_url_kwarg = 'post_slug'
