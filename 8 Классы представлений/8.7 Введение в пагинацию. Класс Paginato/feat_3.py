# Подвиг 3. Из входного потока читается список строк с помощью следующей команды:
#
# lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять
# Объявите переменную pages, которая ссылается на объект пагинатора (Paginator) для списка lst с разбиением по 4 элемента на страницу.
#
# Используя переменную pages и функцию print, выведите на экран в одну строчку через пробел общее число элементов в списке и общее число страниц.


from django.core.paginator import Paginator

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять

pages = Paginator(lst, 4)
print(pages.count, pages.num_pages)
