text = 'здесь что-то написано'  # input('Введите текст: ')
text_dict = dict()

for i_sym in text:
    if i_sym in text_dict:
        text_dict[i_sym] += 1
    else:
        text_dict[i_sym] = 1
# print(f'{text_dict}')

text_dict_invert = dict()
for index in range(max(text_dict.values())):
    text_dict_invert[index + 1] = []

# print(text_dict_invert)

for key, value in text_dict.items():
    text_dict_invert[value].append(key)

for key, value in text_dict_invert.items():
    print(f'{key} : {value}')
