text = input('Введите текст: ')
vowels = 'аиеёоуыэюя'
vowels_in_text = []
for letter in text:
    if letter in vowels:
        vowels_in_text.append(letter)

print(f'Список гласных букв: {vowels_in_text}')
print(f'Длина списка: {len(vowels_in_text)}')
