# Подвиг 6. С помощью объекта cache:
#
# from django.core.cache import cache
# сохраните в кэше данные с ключом 'https://proproprogs.ru' и значением 'Главная страница'. Время хранения кэша выберите самостоятельно, но не менее одной минуты.


from django.core.cache import cache

cache.set('https://proproprogs.ru', 'Главная страница', timeout=60)
