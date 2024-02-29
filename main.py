import src.utils


temp = src.utils.open_file__extract_info()    # Присваиваю переменной temp данные из файла json


temp = src.utils.reformate_date(temp)   # Форматирую дату и время для дальнейшей сортировки
temp = src.utils.sort_by_date_time(temp)    # Сортирую по дате и времени в обратном порядке
temp = src.utils.hide_from(temp)    # Маскирую отправителя
temp = src.utils.hide_to(temp)    # Маскирую получателя
temp = src.utils.reverse_date(temp)    # Переварачиваю дату на привычный лад


src.utils.print_result(temp)    # Вывожу на экран результат
