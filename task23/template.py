def f(s, fn):
    if s < fn or s == 12:
        return 0
    if s == fn:
        return 1
    m = [f(s + 1, fn)]
    if s % 2:
        m.append(f(s // 2, fn))
    return sum(m)


print(f(2, 9) * f(9, 15))