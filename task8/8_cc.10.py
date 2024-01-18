from itertools import product

words = [''.join(word) for word in product(sorted('ластик'), repeat=5)]
k = 0
for word in words:
    temp = word.replace('и', 'а').replace('с', 'л').replace('т', 'л').replace('к', 'л')
    if not ('касса' <= word <= 'такса') and 'аа' not in temp and 'лл' not in temp:
        k += word.count('т')
print(k)