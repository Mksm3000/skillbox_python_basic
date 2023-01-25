while True:
    password = input('Придумайте пароль: ')
    uppers = len([symbol for symbol in password if symbol.isupper()])
    digits = len([symbol for symbol in password if symbol.isdigit()])
    if len(password) < 8:
        print('Пароль должен быть минимум из восьми символов.')
    elif uppers < 1:
        print('Пароль должен содержать хотя бы одну большую букву.')
    elif digits < 3:
        print('Пароль должен содержать хотя бы три цифры.')
    else:
        print('Отлично! Теперь это надёжный пароль!')
        break