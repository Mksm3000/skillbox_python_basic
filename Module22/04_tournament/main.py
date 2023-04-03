import os


def filt(mrk, lst):
    filt_list = []
    for data in lst:
        if int(data[2]) >= int(mrk):
            name = []
            fio = data[1][:1] + '. ' + data[0] + ' ' + data[2]
            name.append(fio)
            filt_list.append(name)
    return filt_list


def sort_by_mark(strk):
    return strk[-2:]


helper = list()

file = open('first_tour.txt', 'r', encoding='utf-8')
for line in file:
    helper.append(line.split())
file.close()

#print(helper)

mark = helper[0][0]
filt_list = filt(mark, helper[1:])
filt_list.sort(key=sort_by_mark, reverse=True)
#print(filt_list)

file_second = open('second_tour.txt', 'w', encoding='utf-8')
file_second.write(str(len(filt_list)) + '\n')

row_num = 1
for row in filt_list:
    file_second.write(str(row_num) + ') ' + str(*row) + '\n')
    row_num += 1

file_second.close()