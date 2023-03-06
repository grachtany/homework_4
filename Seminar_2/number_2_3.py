N = int(input('Введите общее число дней:'))
res = 0

for i in range(N):
    temp = int(input('Введите температуру: '))
    if temp >= 0:
         res += 1
else:
    b = res
    res = 0
print(b)