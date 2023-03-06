from random import randint

N = int(input('Введите количество чисел в первом множестве: '))
K = int(input('Введите количество чисел в втором множестве: '))

n = set([randint(1, 10) for _ in range(N)])
print(n)
k = set([randint(1, 10) for _ in range(K)])
print(k)

L = n.intersection(k)
print(L)
print(sorted(L))