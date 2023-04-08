# - Присутствуют все три поля.
# - Поле «Имя» содержит только буквы.
# - Поле «Имейл» содержит @ и . (точку).
# - Поле «Возраст» является числом от 10 до 99.
#
# В результате проверки сформируйте два файла:
#
# - `registrations_good.log` — для правильных данных, записывать строки в том виде, как есть;
# - `registrations_bad.log` — для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных напишите функцию, которая может выдавать исключения:
#
# - НЕ присутствуют все три поля: `IndexError`.
# - Поле «Имя» содержит НЕ только буквы: `NameError`.
# - Поле «Имейл» НЕ содержит @ и . (точку): `SyntaxError`.
# - Поле «Возраст» НЕ является числом от 10 до 99: `ValueError`.
#
# **Формат выходных данных**
# ```
# Содержимое файла registrations_bad.log:
# Ольга kmrn@gmail.com 123		Поле «Возраст» НЕ является числом от 10 до 99
# Чехова kb@gmail.com 142		Поле «Возраст» НЕ является числом от 10 до 99
# ……
# Степан ky 59		Поле «Имейл» НЕ содержит @ и . (точку)
# ……
#
# Содержимое файла registrations_good.log:
# Геннадий ttdababmt@gmail.com 69
# Ольга ysbxur@gmail.com 20

def valid(data):
    if len(data) != 3:
        return IndexError
    elif not data[0].isalpha():
        return NameError
    elif '@' not in data[1] or '.' not in data[1]:
        return SyntaxError
    elif int(data[2]) < 10 or int(data[2]) > 99:
        return ValueError
    # except IndexError as index_err:
    #     error_str += 'НЕ присутствуют все три поля. '
    # except NameError as name_err:
    #     error_str += 'Поле «Имя» содержит НЕ только буквы. '
    # except SyntaxError as syn_err:
    #     error_str += 'Поле «Имейл» НЕ содержит @ и . (точку). '
    # except ValueError as val_err:
    #     error_str += 'Поле «Возраст» НЕ является числом от 10 до 99. '
    else:
        return 'None'


file = open('registrations_bad.log', 'w')
file.close()

file = open('registrations_good.log', 'w')
file.close()

with open('registrations.txt', 'r', encoding='utf-8') as file_reg:
    for line in file_reg:
        line = line.rstrip('\n')
        line_list = line.split()
        result = valid(line_list)
        if result == IndexError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as file_bad:
                file_bad.write(line + '\t' + 'НЕ присутствуют все три поля.' + str(result) + '\n')
        elif result == NameError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as file_bad:
                file_bad.write(line + '\t' + 'Поле «Имя» содержит НЕ только буквы.' + str(result) + '\n')
        elif result == SyntaxError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as file_bad:
                file_bad.write(line + '\t' + 'Поле «Имейл» НЕ содержит @ и . (точку).' + str(result) + '\n')
        elif result == ValueError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as file_bad:
                file_bad.write(line + '\t' + 'Поле «Возраст» НЕ является числом от 10 до 99.' + str(result) + '\n')
        elif result == 'None':
            with open('registrations_good.log', 'a', encoding='utf-8') as file_good:
                file_good.write(line + '\n')
