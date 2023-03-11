students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def function(dict):
    list_of_interests = []
    summ_of_surnames = 0
    for i_student in dict:
        list_of_interests += (dict[i_student]['interests'])
        summ_of_surnames += len(dict[i_student]['surname'])
    return list_of_interests, summ_of_surnames


pairs = [] #пара "ID студента — возраст"
for id in students:
    pair = id, students[id]['age']
    pairs.append(pair)
print(f'\nСписок пар «ID студента — возраст»: {pairs}')
interests, summ = function(students)
print(f'Полный список интересов всех студентов: {interests}')
print(f'Общая длина всех фамилий студентов:  {summ}')
