# Подвиг 6. На вход подается строка с заголовком страницы:

# title_page = input()
# Необходимо удалить из строки title_page все символы двоеточий, используя стандартный фильтр фреймворка Django (подумайте какой). Результирующую строку вывести в консоль.


from django.template.defaultfilters import cut

title_page = input()
print(cut(title_page, ":"))
