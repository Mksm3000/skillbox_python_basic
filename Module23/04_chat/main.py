
while True:
    name = input('\nВведите ваше имя: ')
    print('1. Посмотреть текущий текст чата.\n2. Отправить сообщение.\n')
    choice = int(input('Введите номер действия: '))
    if choice == 1:
        print('\nТекущий текст чата:')
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file_chat:
                for line in file_chat:
                    line = line.rstrip('\n')
                    print(line)
        except FileNotFoundError:
            print('Чат пока пустой. Вы - первыйнах!')
    elif choice == 2:
        message = input('Введите текст сообщения: ')
        with open('chat.txt', 'a', encoding='utf-8') as file_input:
            file_input.write(name + ': ' + message + '\n')
