# Подвиг 7. На вход подается строка из пунктов меню, записанных через точку с запятой:

# menu = list(map(str.strip, input().split(";")))
# С помощью стандартных фильтров фреймворка Django необходимо выбрать первый и последний элементы списка menu и вывести их в консоль в виде одной строки в формате:

# <первый элемент> <последний элемент>


from django.template.defaultfilters import cut

menu = list(map(str.strip, input().split(";")))
print(menu[0], menu[-1])
