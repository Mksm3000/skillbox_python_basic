text = input('Введите строку: ').split()
longest = ''
len_max = 0
for word in text:
    if len(word) > len_max:
        longest = word
        len_max = len(word)

print('Самое длинное слово:', longest)
print('Длина этого слова:', len(longest))
