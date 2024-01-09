def f(line):
    while '12' in line or '332' in line or '222' in line:
        if '12' in line:
            line = line.replace('12', '2', 1)
        if '322' in line:
            line = line.replace('322', '21', 1)
        if '222' in line:
            line = line.replace('222', '3', 1)

    k = len(line)
    return k


a = []
for n in range(4, 1000):
    a.append(f('1' + '2' * n))
print(max(a))
