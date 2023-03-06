def simple_num(b):
    if b == [2, 3]:
        return True
    else:
        if b % 2 == 0 or b < 2:
            return False
        for i in range(3, int(b**0.5) + 1, 2):
            if b % i == 0:
                return False
        return True


print(simple_num(int(input('Введите число: '))))
