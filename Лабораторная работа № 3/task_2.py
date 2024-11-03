# Функция для поиска общих участников
def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    # Разделяем строки на списки участников по заданному разделителю
    first_group_list = participants_first_group.split(delimiter)
    second_group_list = participants_second_group.split(delimiter)

    # Находим общих участников
    common_participants = set(first_group_list).intersection(second_group_list)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


# Пример использования с разделителем по умолчанию (запятая)
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)  # Ожидаемый результат: ['Петров', 'Сидоров']

# Пример использования с другим разделителем (например, |)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(common_participants)  # Ожидаемый результат: ['Петров', 'Сидоров']

