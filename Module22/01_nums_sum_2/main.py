summa = 0

file = open('numbers.txt', 'r')

for row in file:
    data = row.strip()
    if data != "":
        summa += int(data)
file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(str(summa))
answer_file.close()