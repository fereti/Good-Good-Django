# Подвиг 4 (на повторение). Необходимо продолжить программу для объявления включающего шаблонного тега (inclusion tag), использующего шаблон 'women/mainmenu.html', и реализованного в виде функции show_list(), которая не имеет никаких параметров и передающая в указанный шаблон данные в виде словаря:
#
# {'items': ['about', 'contact', 'docs']}
# P.S. В программе нужно только создать включающий тег. Вызывать его не нужно.


from django import template

register = template.Library()


@register.inclusion_tag('women/mainmenu.html')
def show_list():
    return {'items': ['about', 'contact', 'docs']}
