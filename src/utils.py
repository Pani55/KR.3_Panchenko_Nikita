import json
from datetime import datetime


def open_file__extract_info():
    """
    Функция достаёт информацию из файла,
    затем корректирует её для удобной работы в дальнейшем,
    убирая из списка пустые словари и отменённые транзакции.

    :return: Возвращает скорректированный массив данных.
    """

    with open("operations.json", 'r', encoding='utf-8') as file:
        temp = json.load(file)
        lst = []
        for line in temp:
            if "state" not in line or line['state'] == 'CANCELED':
                continue
            else:
                lst.append(line)

    return lst

def reformate_date(temp):
    """
    Функция изменяет формат записи даты и времени для дальнейшей сортировки.

    :param temp: массив данных для форматирования.
    :return: отформатированный массив.
    """

    for line in temp:
        line['date'] = line['date'][:10] + ' ' + line['date'][11:]

    return temp

def sort_by_date_time(temp):
    """
    Функция сортирует массив по дате и времени.

    :param temp: массив для сортировки.
    :return: массив после сортировки.
    """

    result = sorted(temp, reverse=True, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M:%S.%f"))

    return result
