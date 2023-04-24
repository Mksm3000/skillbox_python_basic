import random


class Student:

    def __init__(self, surname, name, group, marks):
        self.surname = surname
        self.name = name
        self.group = group
        self.marks = marks

    def info(self):
        print(f'ФИ: {self.surname} {self.name}. '
              f'Группа: {self.group}. Успеваемость: {self.marks}. '
              f'Средний балл: {self.mark_mid()}')

    def mark_mid(self):
        return sum(self.marks) / len(self.marks)


surname = ['Petrov', 'Ivanov', 'Smirnov', 'Sidorov', 'Chekhov', 'Bulgakov', 'Mishin', 'Osipov', 'Klimov']
name = ['Boris', 'Vova', 'Gena', 'Dima', 'Egor', 'Maksim', 'Petya', 'Denis', 'Pasha', 'Sergey']

student_list = []

for _ in range(10):
    student = Student(
        surname = random.choice(surname),
        name = random.choice(name),
        group = random.randint(1, 5),
        marks = [random.randint(3, 10) for _ in range(5)]
    )
    student_list.append(student)

student_list.sort(key=Student.mark_mid)

for student in student_list:
    student.info()
