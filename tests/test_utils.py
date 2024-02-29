from src.utils import reformate_date, hide_from, hide_to, reverse_date, sort_by_date_time, print_result


def test_reformate_date():
    assert reformate_date([{'date': "2018-08-19T04:27:37.904916"}]) == [{'date': '2018-08-19 04:27:37.904916'}]


def test_hide_from():
    assert hide_from([{'from': "Visa Classic 6831982476737658"}]) == [{'from': "Visa Classic 6831 98** **** 7658"}]
    assert hide_from([{'from': "Счет 48894435694657014368"}]) == [{'from': "Счет **4368"}]
    assert hide_from([{}]) == [{}]


def test_hide_to():
    assert hide_to([{'to': "Visa Platinum 8990922113665229"}]) == [{'to': "Visa Platinum 8990 92** **** 5229"}]
    assert hide_to([{'to': "Счет 38976430693692818358"}]) == [{'to': "Счет **8358"}]


def test_reverse_date():
    assert reverse_date([{'date': '2018-08-19 04:27:37.904916'}]) == [{'date': '19.08.2018'}]


def test_sort_by_date_time():
    assert sort_by_date_time([{'date': '2018-08-19 04:27:37.904916'},
                              {'date': '2019-05-23 02:45:55.564155'}]) == [{'date': '2019-05-23 02:45:55.564155'},
                                                                           {'date': '2018-08-19 04:27:37.904916'}]


def test_print_result():
    assert print_result([{"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230",
                          "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
                          "description": "Перевод организации", "from": "Счет 48894435694657014368",
                          "to": "Счет 38976430693692818358"}]) is None
