def max(list):
    max_1 = list[0]
    for i in range(len(list)):
        if max_1 < list[i]:
            max_1 = list[i]
    return max_1

def min(list):
    min_1 = list[0]
    for i in range(len(list)):
        if min_1 > list[i]:
            min_1 = list[i]
    return min_1

n = int(input('Введите количество оценок: '))
list = []
for i in range(n):
    list.append(int(input('Введите оценку: ')))
print(list)

print(max(list))
print(min(list))

for i in range(len(list)):
    if list[i] == max(list):
        list[i] = min(list)
    else: 
        list[i]
    
print(list)
# import random

# n = int(input('Введите количество оценок: '))
# array = [random.randint(1, 5) for i in range(n)]
# print(array)
# num_min = min(array)
# num_max = max(array)
# num = [num_min if i == num_max else i for i in array]
# print(num)