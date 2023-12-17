# Подвиг 7. Необходимо продолжить программу для объявления включающего шаблонного тега (inclusion tag), использующего шаблон 'women/mainmenu.html', и реализованного в виде функции:
#
# def show_list(items=None): ...
# с одним параметром items и передачей в указанный шаблон данные в виде следующего словаря:

# {'items': items}

# P.S. В программе нужно только создать включающий тег. Вызывать его не нужно.


from django import template

register = template.Library()


@register.inclusion_tag('women/mainmenu.html')
def show_list(items=None):
    return {'items': items}
