n = int(input('Введите количество элементов списка: '))
A = list(map(int, input('Введите через пробел элементы списка: ').split()))

if len(A) != n:
    print('Введенное количество элементов списка не соответствует заданному количеству')
else:
    n = int(input('Введите искомое число: '))
    count = 0

    for i in range(len(A)):
        if A[i] == n:
            count +=1
    print(count)