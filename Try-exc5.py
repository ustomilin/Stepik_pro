week = { 1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье", }

def get_weekday(number):
    try:
        if type(number) != int:
            raise TypeError('Аргумент не является целым числом')
        else:
            return week[number]
    except KeyError:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')