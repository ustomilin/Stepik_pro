def fuu(c1, operator, c2):
   if operator == 'plus':
       return int(c1) + int(c2)
   elif operator == 'minus':
       return c1 - c2
   elif operator == 'times':
       return int(c1)*int(c2)
   else:
       try:
           return c1//c2
       except ZeroDivisionError:
           return 'Sorry'


def zero(oper = None):
    if oper == None:
        return 0
    return fuu(0, oper[0], oper[1])

def one(oper = None):
    if oper == None:
        return 1
    return fuu(1, oper[0], oper[1])
def two(oper = None):
    if oper == None:
        return 2
    return fuu(2, oper[0], oper[1])
def three(oper = None):
    if oper == None:
        return 3
    return fuu(3, oper[0], oper[1])
def four(oper = None):
    if oper == None:
        return 4
    return fuu(4, oper[0], oper[1])
def five(oper = None):
    if oper == None:
        return 5
    return fuu(5, oper[0], oper[1])
def six(oper = None):
    if oper == None:
        return 6
    return fuu(6, oper[0], oper[1])
def seven(oper = None):
    if oper == None:
        return 7
    return fuu(7, oper[0], oper[1])
def eight(oper = None):
    if oper == None:
        return 8
    return fuu(8, oper[0], oper[1])
def nine(oper = None):
    if oper == None:
        return 9
    return fuu(9, oper[0], oper[1])


def plus(x):
    return ('plus', x)
def minus(x):
    return ('minus', x)
def times(x):
    return ('times', x)
def divided_by(x):
    return ('divided_by', x)

print(seven(times(five())))