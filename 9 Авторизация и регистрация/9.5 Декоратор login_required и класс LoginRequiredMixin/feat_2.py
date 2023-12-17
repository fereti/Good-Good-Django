# Подвиг 2. Пусть имеется следующая функция представления:
#
# # from django.contrib.auth.decorators import login_required
#
# def show_post(request, post_slug):
#     post = {'title': "Статья", 'slug': post_slug, 'content': "Содержимое статьи"} # заглушка для get_object_or_404(Subject, slug=post_slug)
#
#     data = {
#         'title': post['title'],
#         'post': post,
#     }
#
#     return render(request, 'subject/post_detail.html', context=data)
# Примените к ней декоратор login_required, чтобы запретить просмотр неавторизованным пользователям.


from django.contrib.auth.decorators import login_required


@login_required
def show_post(request, post_slug):
    post = {'title': "Статья", 'slug': post_slug,
            'content': "Содержимое статьи"}  # заглушка для get_object_or_404(Subject, slug=post_slug)

    data = {
        'title': post['title'],
        'post': post,
    }

    return render(request, 'subject/post_detail.html', context=data)
