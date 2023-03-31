from zipfile import ZipFile

file_name = str()
with ZipFile('voyna-i-mir.zip', 'r') as myzip:
    for item in myzip.namelist():
        file_name = item

with ZipFile('voyna-i-mir.zip', 'r') as myzip:
    myzip.extractall()

myzip.close()

file = open(file_name, 'r', encoding='utf-8')

letter_dict = dict()
for letter in file.read():
    if letter.isalpha():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

file.close()

letter_list = []
for key, value in letter_dict.items():
    letter_list.append([key, value])

def right(data):
    return data[1]


letter_list.sort(key=right,reverse=True)

result = open('result.txt', 'w', encoding='utf-8')

for element in letter_list:
    result.write(str(element[0]) + ': ' + str(element[1]) + '\n')

result.close()
