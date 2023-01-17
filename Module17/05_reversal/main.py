def search(text):
    i_min = 0
    i_max = 0
    count = 0
    count_h = 0
    for index in text:
        if index == 'h' and count_h == 0:
            i_min = count
            count_h += 1
        elif index == 'h' and count_h > 0:
            i_max = count
            count_h += 1
        count += 1
    return i_min, i_max

        #01234567
text1 = 'hqwehrty' # Развёрнутая последовательность между первым и последним h: ewq.
text2 = 'hh' # Развёрнутая последовательность между первым и последним h:
text3 = 'hhqwerh' # Развёрнутая последовательность между первым и последним h: rewqh.

test = text3 # меняем номер строки здесь
min, max = search(test)
# print('min', min)
# print('max', max)
print(f'# Развёрнутая последовательность между первым и последним h: {test[-(len(test)-max+1):-min:-1]}')