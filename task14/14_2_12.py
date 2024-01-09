for p in range(9, 1000):
    for x in range(p):
        a1 = 6 * p ** 3 + x * p ** 2 + 5 * p + x
        a2 = 1 * p ** 3 + x * p ** 2 + 6 * p + 5
        for y in range(1, p):
            for z in range(p):
                a3 = y * p ** 2 + 8 * p + z
                if a1 + a2 == a3:
                    print(x * p ** 2 + y * p + z)