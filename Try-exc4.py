def open_file(file_name):
    try:
        x = open(file_name)
        print(x.read())
        x.close()
    except FileNotFoundError:
        print('Файл не найден')

open_file(input())