def f(s):
    while "18" in s or "388" in s or "888" in s:
        if "18" in s:
            s = s.replace("18", "8", 1)
        if "388" in s:
            s = s.replace("388", "81", 1)
        if "888" in s:
            s = s.replace("888", "3", 1)

    k = s.count('1')
    return k


for n in range(4, 10000):
    if f('1' + '8' * n) == 3:
        print(n)

