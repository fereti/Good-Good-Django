# Подвиг 5. На вход подается строка с заголовком страницы:

# title_page = input()
# Необходимо преобразовать этот заголовок в слаг (slug), используя стандартный фильтр slugify фреймворка Django. Результирующую строку вывести в консоль.


from django.template.defaultfilters import slugify

title_page = input()

print(slugify(title_page))
