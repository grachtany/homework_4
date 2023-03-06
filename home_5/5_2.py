def sum(a, b):
    a += 1
    b -= 1    
    if b == 0:
        return a
    return sum(a, b )


A = int(input('Введите число a: '))
D = int(input('Введите число b: '))

print(sum(A, D))
