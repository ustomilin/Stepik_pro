def get_id(names, name: str):
    #по условию, имя - строка
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    #по условию - имя только из латинских букв и написано с большой буквы
    elif name != name.capitalize() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    else:
        return len(names) + 1

names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'ruslan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)