# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

list_1 = [1, 2, 3, 2, 3]
# print(list_1)
# list_02 = list(set(list_1))
# print(list_02)
# count = 0

# for i in range(len(list_02)):

#            count += list_1.count(list_02[i])//2
   
# print(count)

dict_list = {}.fromkeys(list_1,0)
print(dict_list)
for i in dict_list:
        dict_list[i] +=1
print([i//2 for i in dict_list.values() if not i %2])