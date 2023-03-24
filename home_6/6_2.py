from random import randint

N = int(input('Введите количество чисел в первом множестве: '))

n = list([randint(1, 10) for _ in range(N)])
print(n)

min_number = int(input("Минимальное значение: "))
max_number = int(input("Максимальное значение: "))
for i in range(len(n)):
    if min_number <= n[i] <= max_number:
        print(i)