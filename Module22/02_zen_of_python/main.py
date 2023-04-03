file = open('zen.txt', 'r', encoding='utf-8')
file_list = []

for line in file:
    file_list.append(line)

file.close()

file_list.reverse()

for element in file_list:
    print(element, end='')
