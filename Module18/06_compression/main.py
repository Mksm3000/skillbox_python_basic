def group(list):
#    print('входящий список', list)
    count = 1
    for i in range(len(list)):
        if i < len(list) - 1:
            if list[i] == list[i + 1]:
                count += 1
            else:
                break
        else:
            break
    return list[i], count


text = list(input('Введите строку: '))
total = ''

while len(text) > 0:
    total += group(text)[0] + str(group(text)[1])
#    print(total)
    text = text[(group(text)[1]):]
#    print(text)

print('Закодированная строка:', total)
