import os

def func(dir):
    files_count = 0
    files_size = 0
    sub_dir_count = 0

    for i_elem in os.listdir(dir):
        dir_in = os.path.join(dir, i_elem)

        if os.path.isfile(dir_in):
            files_count += 1
            files_size += os.path.getsize(dir_in)
        elif os.path.isdir(dir_in):
            sub_dir_count += 1
            result = func(dir_in)
            if result:
                sub_dir_count += result[0]
                files_count += result[1]
                files_size += result[2]
            else:
                break

    return sub_dir_count, files_count, files_size


path = os.path.abspath(os.path.join('..'))
sub_dir_count, files_count, files_size = func(path)

print(f'\n{path}')
print(f'Размер каталога (в Кб): {(files_size/1024)}')
print(f'Количество подкаталогов: {sub_dir_count}')
print(f'Количество файлов: {files_count}')