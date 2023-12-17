# Подвиг 3. Необходимо усовершенствовать предыдущую программу и объявить простой шаблонный тег (simple tag) в виде функции:

# def get_default_title(title="Без заголовка"): ...
# которая принимает один параметр title с начальным значением "Без заголовка" и возвращает его в виде строки.

# P.S. В программе нужно только создать простой тег. Вызывать его не нужно.


from django import template

register = template.Library()


@register.simple_tag()
def get_default_title(title="Без заголовка"):
    return title
