def f(n):
    return 39 * 3 + 4 * n


def f_(n):
    line = '>' + 39 * '0' + n * '1' + 39 * '2'
    while '>1' in line or '>2' in line or '>0' in line:
        if '>1' in line:
            line = line.replace('>1', '22>', 1)
        if '>2' in line:
            line = line.replace('>2', '2>', 1)
        if '>0' in line:
            line = line.replace('>0', '1>', 1)
    return sum(map(int, line[:-1]))


def is_prime(n):
    k = 0
    for i in range(1, n + 1):
        if n % i == 0:
            k += 1
    return k == 2


for i in range(0, 20):
    if is_prime(f_(i)):
        print(i)
# 5
# 8
# 10
# 14
# 16
# 19