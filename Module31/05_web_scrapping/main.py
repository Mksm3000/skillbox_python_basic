import json
import re
import requests
import html


# Ожидаемый результат:
# ['Latest News', 'Useful Links', 'Search', 'Heading 3']
# Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.
#
# Дополнительно:
# найдите любой сайт, у которого в коде есть теги 'h3',
# выполните get-запрос к этому сайту при помощи библиотеки requests
# и получите аналогичный список всех его подзаголовков (заключенных в теги 'h3')

# with open('examples.html', 'r') as f:
#     text = f.read()
#     # print(text)
#     pattern = r'<h3>(.*)</h3>'
#     result = re.findall(pattern, text)
#     print(result)

link = 'https://stackoverflow.com/'
result = requests.get(link)
data = html.unescape(result.text)

with open('test.html', 'w', encoding='utf-8') as file:
    file.write(data)

with open('test.html', 'r', encoding='utf-8') as r_file:
    text = r_file.read()
    print(text)
    pattern = r'<h3.*>(.*)</h3>'
    result = re.findall(pattern, text)
    print(result)
