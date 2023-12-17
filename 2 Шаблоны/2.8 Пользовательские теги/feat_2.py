# Подвиг 2. Необходимо продолжить программу для объявления простого шаблонного тега (simple tag) в виде функции get_default_title(), которая не имеет никаких параметров и возвращает строку "Заголовок по умолчанию".
# P.S. В программе нужно только создать простой тег. Вызывать его не нужно.


from django import template

register = template.Library()


@register.simple_tag()
def get_default_title():
    return 'Заголовок по умолчанию'
