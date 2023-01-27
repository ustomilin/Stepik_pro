import json

def print_json(file_name):
    try:
         with open(file_name) as file:
            file_sod = json.load(file)
            print(file_sod)
    except ValueError:
         print('Ошибка при десериализации')
    except FileNotFoundError:
        print('Файл не найден')

print_json(input())