flag = True
while flag:
    adress = input('\nВведите IP: ').split('.')
    if len(adress) != 4:
         print('Адрес — это четыре числа, разделённые точками.')
    else:
        for i in range(len(adress)):
            part = adress[i]
            if not part.isdigit():
                print(f'{part} — число указано не верно.')
                break
            if int(part) > 255:
                print(f'{part} — число указано не верно.')
                break
        else:
            flag = False
print('IP-адрес корректен.')