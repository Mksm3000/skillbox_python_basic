# Введите количество пар слов: 3
# Первая пара: Привет - Здравствуйте
# Вторая пара: Печально - Грустно
# Третья пара: Весело - Радостно
#
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет

synon_dict = dict()

number = int(input('Введите количество пар слов: '))
for i in range(number):
    print(f'{i + 1}-я пара:', end = ' ')
    pair = input().lower().split(' - ')
    synon_dict[pair[0]] = pair[1]
print(synon_dict)

while True:
    word = input('\nВведите слово: ').lower()
    if word in synon_dict.keys():
        print(f'Синоним: {(synon_dict[word]).capitalize()}')
        break
    elif word in synon_dict.values():
        print(f'Синоним: {(list(synon_dict.keys())[list(synon_dict.values()).index(word)]).capitalize()}')
        break
    print('Такого слова в словаре нет.')
