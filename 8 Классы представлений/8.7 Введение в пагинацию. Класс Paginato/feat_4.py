# Подвиг 4. Из входного потока читается список строк с помощью следующей команды:
#
# lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять
# Объявите переменную pages, которая ссылается на объект пагинатора (Paginator) для списка lst с разбиением по 3 элемента на страницу.
#
# Используя переменную pages и итератор page_range, с помощью оператора for выведите по порядку (возрастания) номера страниц в одну строчку через пробел.


from django.core.paginator import Paginator

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять

pages = Paginator(lst, 3)
print(*[i for i in pages.page_range])
