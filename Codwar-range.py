def solution(args):
    x = []
    while args:
        y = []
        for i in range(len(args)-1):
            y.append(args[i])
            if args[i] + 1 == args[i+1] and args[i+1] != args[-1]:
                continue
            else:
                args = args[i+1:]
                break
        ku = ''
        if len(args) == 1:
            if args[0] == y[-1] +1:
                y.append(args[0])
            else:
                ku = str(args[0])
            args = []
        if len(y) == 2:
            x.append(str(y[0]))
            x.append(str(y[1]))

        elif len(y) == 1:
            x.append(str(y[0]))
        else:
            x.append(f'{y[0]}-{y[-1]}')
        if ku:
            x.append(ku)
    return ','.join(x)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))