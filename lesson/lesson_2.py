list_1 = []  # пустой список
list_2 = list()  # функция список
list_3 = [1, 2, 3, 5]
print(list_1)
print(list_2)
print(list_3)  # вывел список массивом
print(*list_3)  # вывод список без запятыхб только значения

# Перебор чисел
for i in list_3:
    print(list_3)

print(len(list_3))  # Узнать число  элементов
print(list_3[3])  # узнать элемент под номером

list_3.append(8)  # добавление элемента в rконец списка
print(list_3)


for i in range(5):
    list_1.append(i)
    print(list_1)

list.pop # Удаление последнего элемента
list_3.insert(2, 11) #Вставление на индекса элемента
print(list_3)

# Кортеж
t = ()

print(type(t))

t = (1, 5,3, ) # В конце кортежа обязательно ,
print(type(t))
