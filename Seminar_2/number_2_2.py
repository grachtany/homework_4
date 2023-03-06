A = int(input("Введите число: "))

fib1 = 0
fib2 = 1
i = 2

while A >= fib2:
    if A == fib2:
        print(i)
        break
    fib1, fib2 = fib2, fib1 + fib2
    i += 1
else:
    print(-1)
