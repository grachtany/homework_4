def stepen(a, b):
    if b == 0:
        return 1
    if b < 0:
        return stepen(a, b + 1)*1 / a
    return stepen(a, b-1) * a


A = int(input('Введите число, которое будем возводить в степень: '))
D = int(input('Введите степень: '))

print(stepen(A, D))
