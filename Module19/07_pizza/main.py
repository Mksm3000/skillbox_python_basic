# Введите количество заказов: 6
# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5
#
# Иванов:
# 	Мексиканская: 2
# 	Мясная: 3
# 	Пепперони: 3
# Петров:
# 	Де-Люкс: 2
# 	Интересная: 5


orders = int(input('Введите количество заказов: '))
clients_dict = {}

for i in range(orders):
    print(f'{i + 1} заказ:', end=' ')
    clients_str = input().split()
    family = clients_str[0]
    pizza = clients_str[1]
    quant = int(clients_str[2])

    if family not in clients_dict.keys():
        clients_dict[family] = {pizza: quant}
    elif family in clients_dict.keys():
        if pizza in clients_dict[family].keys():
            clients_dict[family][pizza] += quant
        else:
            clients_dict[family][pizza] = quant

for key, value in clients_dict.items():
    print(f'\n{key}:')
    for key_sub, value_sub in sorted(value.items()):
        print(f'\t{key_sub}: {value_sub}')
