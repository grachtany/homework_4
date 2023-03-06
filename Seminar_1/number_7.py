n = int(input('Введите год- '))

if (n%4 == 0 and (not n%100 == 0 )) or n%400 == 0  :
    print(f"{n} - високосный год") 
else: print(f"{n} - Не високосный год") 