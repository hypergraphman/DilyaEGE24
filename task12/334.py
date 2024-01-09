def f(a):
    while '25' in a or '355' in a or '555' in a:
        if '25' in a:
            a = a.replace('25', '32', 1)
        if '355' in a:
            a = a.replace('355', '25', 1)
        if '555' in a:
            a = a.replace('555', '3', 1)
    return a


for n in range(4, 2000):
    line = '3' + '5' * n
    if f(line).count('2') == 5:
        print(n)
