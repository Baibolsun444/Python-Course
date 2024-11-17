import json

INPUT_FILE = "input.json"


def task() -> float:
    # Открываем файл и считываем его содержимое
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    # Проверяем, что данные — это список словарей
    if not isinstance(data, list):
        raise ValueError("Ожидался список словарей в JSON файле.")

    # Суммируем произведения "score" * "weight" для каждого словаря
    total = sum(item["score"] * item["weight"] for item in data if "score" in item and "weight" in item)

    # Возвращаем сумму, округленную до 3 знаков
    return round(total, 3)


# Вызываем функцию и печатаем результат
print(task())

