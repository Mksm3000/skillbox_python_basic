file = open('text.txt', 'r', encoding='utf-8')

letter_dict = dict()
for letter in file.read():
    if letter.isalpha():
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

file.close()

#print(letter_dict)
letter_summ = sum(letter_dict.values())

for key, value in letter_dict.items():
    letter_dict[key] = round(value/letter_summ, 3)
#print(letter_dict)


count_dict = dict()
for key, value in letter_dict.items():
    if value in count_dict:
        pop_data = count_dict.pop(value)
        merge_data = key + pop_data
        count_dict[value] = ''.join(sorted(merge_data))
    else:
        count_dict[value] = key

#print(count_dict)

file = open('analysis.txt', 'w', encoding='utf-8')

for key, value in count_dict.items():
    for element in value:
        file.write(str(element) + ' ' + str(key) + '\n')

file.close()