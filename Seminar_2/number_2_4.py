N = int(input('Введите количество арбузов: '))
min = 1000
max = 0
for i in range(N):
    massa = int(input('Введите массу арбуза: '))
    if massa <= min:
        min = massa
    if massa >= max:
        max = massa
print (f'ИВ возьмет себе арбуз массой {max}')
print (f'ИВ возьмет теще арбуз массой {min}')