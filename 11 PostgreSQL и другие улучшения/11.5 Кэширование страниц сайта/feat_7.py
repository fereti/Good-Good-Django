# Подвиг 7. Пусть в кэш через объект cache были сохранены данные с ключом 'https://sitewomen.ru'. Прочитайте данные по этому ключу и выведите их в консоль.


data = cache.get('https://sitewomen.ru')
print(data)
