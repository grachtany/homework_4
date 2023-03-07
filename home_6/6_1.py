a1 = int(input('1 член: '))
d = int(input('разность: '))
n = int(input('Количество элементов: '))
# Вывод элементов прогрессии в строку
# i = int()
# for i in range(1, n+1):
#     an = a1+d*(i-1)
#     print(an, end=' ')

    
list1 = []
for i in range(1, n+1):
    an = a1+d*(i-1)
    list1.append(an)
    
print(list1)    