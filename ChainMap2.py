from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

eat = ChainMap(bread, meat, sauce, vegetables, toppings)

what = Counter(input().split(','))
#print(what)
itogo = sum(map(lambda x: eat[x[0]]*x[1], what.items()))
#print(itogo)
maxlen = len(max(what.keys(), key = len))
lenpun = 0
for i in sorted(what.items()):
    st = f'{i[0].ljust(maxlen)} x {i[1]}'
    if len(st) > lenpun:
        lenpun = len(st)
    print(st)
itogst = f'ИТОГ: {itogo}р'
if len(itogst) > lenpun:
    lenpun = len(itogst)
print('-'*lenpun)
print(itogst)