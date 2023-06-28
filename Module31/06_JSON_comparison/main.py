import json

diff_list = ['services', 'staff', 'datetime']


def comparison(dict_new, dict_old, text):
    answer = None
    if text in dict_new:
        if dict_new.get(text) != dict_old.get(text):
            answer = dict_new.get(text)
            return answer
    for key, value in dict_new.items():
        if isinstance(value, dict):
            answer = comparison(dict_new[key], dict_old[key], text)
            if answer:
                return answer
    return answer


result = {}
with open('json_new.json', mode='r', encoding='utf-8') as file_new:
    data_new = json.load(file_new)

    with open('json_old.json', mode='r', encoding='utf-8') as file_old:
        data_old = json.load(file_old)

        for element in diff_list:
            if comparison(data_new, data_old, element):
                result[element] = comparison(data_new, data_old, element)

print(result)

with open('result.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, indent=4)

# В консоли должно вывестись следующее сообщение:
# {'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit':
# 1500, 'first_cost': 1500, 'amount': 1}], 'datetime': '2022-01-25T13:00:00+03:00'}
# Помимо вывода в консоль, должен быть сформирован JSON-файл с получившимся словарём (
# result.json).
# Обратите внимание: в result представлены не все изменившиеся поля, а лишь те,
# что объявлены в diff_list.
