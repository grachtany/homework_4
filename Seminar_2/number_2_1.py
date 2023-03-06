n = int(input("Введите неотрицательное число: "))
i = 1
res = 1
while n >= i:
    res = res*i
    i = i+1
print(res)