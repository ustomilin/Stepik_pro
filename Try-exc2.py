from calendar import month_name


try:
    month_num = int(input())
    if month_num not in range(1,13):
        print('Введено число из недопустимого диапазона')
        pass
    print(month_name[month_num])
except ValueError:
    print('Введено некорректное значение')