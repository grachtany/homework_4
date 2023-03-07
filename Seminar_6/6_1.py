list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]
list_3 = []
# n = int(input('Введите количество элементов первого массива: '))
# for i in range(n):
#     list_1.append(int(input('Введите элемент 1-ого массива: ')))
print(list_1)
# k = int(input('Введите количество элементов второго массива: '))
# for i in range(k):
#     list_2.append(int(input('Введите элемент 2-ого массива: ')))
print(list_2)
# for i in list_1:
#     if i not in  list_2:
#         list_3.append(i)
# print(list_3)

print([i for i in list_1 if i not in set(list_2)])
