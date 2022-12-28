# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
my_f = open("result.txt", "a+")
k = int(input("Введите число:   "))
lst = [random.randint(0,100) for i in range(k + 1)]
print(lst)
x = ""
for i in range(k + 1):
    if i < k:
        x += str(lst[i]) + "*x" + str(k-i)  +  " + " 
    else:
        x += str(lst[i])
print(x)

my_f.write(f'{x}  \n')
my_f.close()