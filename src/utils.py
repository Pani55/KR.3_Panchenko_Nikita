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


def hide_from(temp):
    """
    Функция маскирует отправителя

    :param temp: массив данных
    :return: массив с замаскированным отправителем
    """

    for line in temp:
        if 'from' in line:
            if 'Счет' in line['from']:
                line['from'] = 'Счет **' + line['from'][-4:]
            else:
                line['from'] = line['from'][:-12] + ' ' + line['from'][-12:-10] + '** **** ' + line['from'][-4:]
        else:
            continue

    return temp


def hide_to(temp):
    """
    Функция маскирует получателя

    :param temp: массив данных
    :return: массив с замаскированным получателем
    """

    for line in temp:
        if 'Счет' in line['to']:
            line['to'] = 'Счет **' + line['to'][-4:]
        else:
            line['to'] = line['to'][:-12] + ' ' + line['to'][-12:-10] + '** **** ' + line['to'][-4:]

    return temp


def reverse_date(temp):
    """
    Функция переворачивают дату

    :param temp: массив данных
    :return: обработанный массив
    """

    for line in temp:
        line['date'] = line['date'][8:10] + '.' + line['date'][5:7] + '.' + line['date'][:4]

    return temp


def sort_by_date_time(temp):
    """
    Функция сортирует массив по дате и времени.

    :param temp: массив для сортировки.
    :return: массив после сортировки.
    """

    result = sorted(temp, reverse=True, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M:%S.%f"))

    return result


def print_result(temp):
    """
    Функция выводит в консоль читаемую информацию о крайних пяти операциях пользователя.

    :param temp: массив данных
    :return: ничего не возвращает, лишь печатает
    """

    counter = 0

    for line in temp:
        if counter != 5:
            if 'from' not in line:
                print(f"{line['date'][:11]} {line['description']}\n"
                      f"Отправитель -> {line['to']}\n"
                      f"{line['operationAmount']['amount']} {line['operationAmount']['currency']['name']}\n")
                counter += 1
            elif 'from' in line:
                print(f"{line['date'][:11]} {line['description']}\n"
                      f"{line['from']} -> {line['to']}\n"
                      f"{line['operationAmount']['amount']} {line['operationAmount']['currency']['name']}\n")
                counter += 1
        else:
            exit()
