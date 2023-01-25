symbols = '~:;<>?!*`#@№$%^&()\|/'
name = input('\nНазвание файла: ')

if name[0] in symbols:
    print('Ошибка: название начинается на один из специальных символов.')
elif not name.endswith('.txt') and not name.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось ".txt" или ".docx".')
else:
    print('Файл назван верно.')
