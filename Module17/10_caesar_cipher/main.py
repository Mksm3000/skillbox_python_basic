def caesar(text, move, alphabet):
    code = ''
    for i in text:
        for j, char in enumerate(alphabet):
            if char == i:
                code += alphabet[(j + move) % len(alphabet)]
            elif j != i and i not in alphabet:
                code += i
                break
    return code


message = input('Введите сообщение: ')
slide = int(input('Введите сдвиг: '))
abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

print(f'Зашифрованное сообщение: {caesar(message, slide, abc)}')
