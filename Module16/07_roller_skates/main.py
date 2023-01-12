def ok_or_not(foot, skate_size):
    for skate in skate_size:
        if foot <= skate:
            return True


skates_count = int(input('Кол-во коньков: '))
skate_size = []

for i in range(skates_count):
    print(f'Размер {i+1}-й пары: ', end=' ')
    size = int(input())
    skate_size.append(size)

mans_count = int(input('\nКол-во людей: '))
foot_size = []

for i in range(mans_count):
    print(f'Размер ноги {i+1}-го человека: ', end=' ')
    size = int(input())
    foot_size.append(size)

foot_size_ok = []

for i in foot_size:
    if ok_or_not(i, skate_size):
        foot_size_ok.append(i)

foot_size_ok.sort()
skate_size.sort()
foot_size_ok.reverse()
skate_size.reverse()

#print('р-ры ног, кому есть коньки ', foot_size_ok)

count = 0
for _ in range(int(len(foot_size_ok)) + int(len(skate_size))):
    for i, foot in enumerate(foot_size_ok):
        for j, skate in enumerate(skate_size):
            if foot <= skate and foot in foot_size_ok:
                foot_size_ok.remove(foot)
                skate_size.remove(skate)
                count += 1
                # print('\nкол-во', count)
                # print('р-ры ног', foot_size_ok)
                # print('р-ры коньков', skate_size)

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count)