def f(x, a):
    return (((x & 26 != 0) or (x & a != 0)) <= (x & 26 != 0)) or ((x & a != 0) and (x & 79 == 0))


for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 10000)):
        print(a)