number = int(input('Количество стран: '))
print('Вводить в строку через пробел (по шаблону: США Вашингтон Бостон Чикаго)')

country_list = []
for i in range(number):
    print(f'{i + 1}-я страна:', end=' ')
    name = input().split()
    country_list.append(name)

country_dict = {country_list[j][0]: country_list[j][1:] for j in range(len(country_list))}

k = 1
while True:
  flag = False
  print(f'\n{k}-й город:', end=' ')
  search = input()
  for country, town in country_dict.items():
    if search in town:
      flag = True
      break
  if flag:
    print(f'Город {search} расположен в стране {country}.')
  else:
    print(f'По городу {search} данных нет.')
  k = k + 1

# Германия Берлин Дрезден Гамбург
# Италия Рим Венеция Милан
# США Вашингтон Бостон Денвер
