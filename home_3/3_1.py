list1 = list()

for i in range(int(input('Введите количecтво символов: '))):
    n = int(input('Введите  число: '))
    list1.append(n)
print(list1)

n = int(input('Введите искомое число: '))
count = 0

for i in range(len(list1)):
    if list1[i] == n:
         count +=1
print(count)
