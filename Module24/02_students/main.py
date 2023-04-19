import random


class Student:
    surname = ''
    name = ''
    group = ''
    marks = []

    def info(self):
        print(f'ФИ: {self.surname} {self.name}. '
              f'Группа: {self.group}. Успеваемость: {self.marks}. '
              f'Средний балл: {self.mark_mid(self.marks)}')

    def mark_mid(self, marks):
        return sum(self.marks) / len(self.marks)


def sort_srednee(i):
    # print(i)
    # print(i[3])
    srednee = sum(i[3]) / len(i[3])
    # print(srednee)
    return srednee


surname = ['Petrov', 'Ivanov', 'Smirnov', 'Sidorov', 'Chekhov', 'Bulgakov', 'Mishin', 'Osipov', 'Klimov']
name = ['Boris', 'Vova', 'Gena', 'Dima', 'Egor', 'Maksim', 'Petya', 'Denis', 'Pasha', 'Sergey']

student_list = [Student() for _ in range(10)]
sort_list = []
for i_element in student_list:
    i_element.surname = random.choice(surname)
    i_element.name = random.choice(name)
    i_element.group = random.randint(1, 5)
    i_element.marks = [random.randint(3, 10) for _ in range(5)]
    data = [i_element.surname, i_element.name, 'Группа №' + str(i_element.group), i_element.marks]
    sort_list.append(data)
    #i_element.info()

# print(sort_list)
sort_list.sort(key=sort_srednee)

for element in sort_list:
    print(*element)
