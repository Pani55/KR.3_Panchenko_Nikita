import src.utils


temp = src.utils.open_file__extract_info()
temp = src.utils.reformate_date(temp)
temp = src.utils.sort_by_date_time(temp)
temp = src.utils.hide_from(temp)
temp = src.utils.hide_to(temp)
temp = src.utils.reverse_date(temp)


src.utils.print_result(temp)
