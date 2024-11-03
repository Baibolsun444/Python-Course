# TODO Напишите функцию для поиска индекса товара
def item_list(items, search_):
    for i, n in enumerate(items):
        if n == search_:
            return i  # Возвращаем индекс первого найденного элемента
    return None  # Если элемент не найден, возвращаем None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = item_list(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
