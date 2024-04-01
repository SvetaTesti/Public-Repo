per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = 100000


def get_deposits(listt, num):
    new_list = list()
    for i in listt.values():
        new_list.append(round(i * num))
    return new_list


deposit = get_deposits(per_cent, money / 100)
max_sum = max(deposit)
print('депозит = ' + str(deposit))
print('Максимальная сумма, которую вы можете заработать — депозит: ' + str(round(max_sum)))
