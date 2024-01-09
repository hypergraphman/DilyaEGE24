def f(a):
    while '52' in a or '2222' in a or '1122' in a:
        if '52' in a:
            a = a.replace('52', '11', 1)
        if '2222' in a:
            a = a.replace('2222', '5', 1)
        if '1122' in a:
            a = a.replace('1122', '25', 1)
    # s = 0
    # for ch in a:
    #     s += int(ch)
    s = int(a)
    return s

mx = 0
ans = None
for n in range(100, 1000):
    line = '1' * n
    if f(line) > mx:
        mx = f(line)
        ans = n
print(ans)

