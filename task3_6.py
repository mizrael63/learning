#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.

import random
SIZE = 100
array = [random.randint(0, SIZE) for _ in range(50)]
reg_1 = SIZE #сюда записываем минимальное число, изначально берем SIZE как максимальное число диапазона
reg_2 = 0 #позиция текущего минимального числа
reg_3 = 0 #максимальное число
reg_4 = 0 #позиция текущего максимального числа
count = 0 #наш счетчик
d = 0 #здесь мы будем складывать
for i in array: #счет максимального и минимального чисел
    if i > reg_3:
        reg_3 = i
        reg_4 = count
    if i < reg_1:
        reg_1 = i
        reg_2 = count
    count += 1

if reg_2 > reg_4: #проверка позиций чисел
    ab = array[reg_4+1:reg_2] #создаем список для суммирования
else:
    ab = array[reg_2+1:reg_4]
for f in ab:
    d = d + f
    
print("В используемом диапазоне:", array, "\nМинимальное число ", reg_1, "находится на месте ", reg_2-1)
print("Максимальное число ", reg_3, "находится на месте ", reg_4)
print("Сумма между минимальным и максимальным элементами массива равна : ", d)
