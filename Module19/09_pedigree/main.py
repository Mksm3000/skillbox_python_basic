count = int(input('Введите количество человек: '))
pedigree = {'Peter_I': 0}
level = 0

for i in range(count - 1):
    print(f'{i + 1}-я пара:', end=' ')
    stroka = input().split()
    potomok = stroka[0]
    predok = stroka[1]
    if predok in pedigree.keys():
        pedigree[potomok] = pedigree[predok] + 1
print('«Высота» каждого члена семьи:')
for key, value in sorted(pedigree.items()):
    print(f'{key} {value}')
