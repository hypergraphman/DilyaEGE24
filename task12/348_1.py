def f(line):
    c = 0
    while '12' in line or '332' in line or '222' in line:
        if '12' in line:
            line = line.replace('12', '2', 1)
        if '322' in line:
            line = line.replace('322', '21', 1)
        if '222' in line:
            line = line.replace('222', '3', 1)

        c += 1

        if c == 2000:
            line = ''
            break

    k = len(line)
    return k


a = []
for n in range(4, 1000):
    line = '1' + '2' * n
    a.append(f(line))
print(max(a))
