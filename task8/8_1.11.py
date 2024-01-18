from itertools import product

words = [''.join(word) for word in product('01234567', repeat=5)]

k = 0
for word in words:
    if word[0] != '0' and word.count('6') == 2 and '61' not in word and '63' not in word and '65' not in word and '67' not in word and '16' not in word and '36' not in word and '56' not in word and '76' not in word:
        k += 1
print(k)