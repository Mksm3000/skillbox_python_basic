import json
import requests

# Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной.
# Ссылка на документацию: https://swapi.dev/
# Внимательно изучите документацию этого API и напишите программу, которая выводит на экран (и в JSON-файл)
# информацию о пилотах легендарного корабля Millennium Falcon.

# Информация о корабле должна содержать следующие пункты:
# 1) название,
# 2) максимальная скорость,
# 3) класс,
# 4) список пилотов.
#
# Внутри списка о каждом пилоте должна быть следующая информация:
# 1) имя,
# 2) рост,
# 3) вес,
# 4) родная планета,
# 5) ссылка на информацию о родной планете.

link = 'https://swapi.dev/api/starships/'
legend = 'Millennium Falcon'
result_dict = {'Starship': {}, 'Pilots': list()}

my_request = requests.get(link)
temp_dict = my_request.json()

starships_list = temp_dict.get('results', [])

legend_dict = {}
for element in starships_list:
    if element.get('name', {}) == legend:
        legend_dict = element


print()
print(f'Name: {legend_dict.get("name")}')
print(f'Max Atmosphering Speed: {legend_dict.get("max_atmosphering_speed")}')
print(f'Starship Class: {legend_dict.get("starship_class")}')
result_dict['Starship']['Name'] = legend_dict.get("name")
result_dict['Starship']['Max Atmosphering Speed'] = legend_dict.get("max_atmosphering_speed")
result_dict['Starship']['Starship Class'] = legend_dict.get("starship_class")


print()
pilots_list = legend_dict.get('pilots')
for pilot_link in pilots_list:
    pilot = {}
    pilot_request = requests.get(pilot_link)
    pilot_dict = pilot_request.json()
    print(f'Name: {pilot_dict.get("name")}')
    print(f'Height: {pilot_dict.get("height")}')
    print(f'Mass: {pilot_dict.get("mass")}')

    planet_request = requests.get(pilot_dict.get("homeworld"))
    planet_dict = planet_request.json()
    print(f'Homeworld: {planet_dict.get("name")} {planet_dict.get("url")}')
    print()
    pilot['Name'] = pilot_dict.get("name")
    pilot['Height'] = pilot_dict.get("height")
    pilot['Mass'] = pilot_dict.get("mass")
    pilot['Homeworld'] = planet_dict.get("name"), planet_dict.get("url")
    result_dict['Pilots'].append(pilot)

# print(result_dict)
# Чтобы в json-файл записать, нужно создать словарь с результатом и записать его в файл
# с помощью open и json.dump

with open('swapi.json', 'w') as file:
    json.dump(result_dict, file, indent=4)
