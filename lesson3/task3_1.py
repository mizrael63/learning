#Задача 1 В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
import random
array = [random.randint(2, 99) for _ in range(99)]
crat_2 = []
crat_3 = []
crat_4 = []
crat_5 = []
crat_6 = []
crat_7 = []
crat_8 = []
crat_9 = []
for i in array:
    if i % 2 == 0:
        crat_2.append(i)
for i in array:
    if i % 3 == 0:
        crat_3.append(i)
for i in array:
    if i % 4 == 0:
        crat_4.append(i)
for i in array:
    if i % 5 == 0:
        crat_5.append(i)
for i in array:
    if i % 6 == 0:
        crat_6.append(i)
for i in array:
    if i % 7 == 0:
        crat_7.append(i)
for i in array:
    if i % 8 == 0:
        crat_8.append(i)
for i in array:
    if i % 9 == 0:
        crat_9.append(i)
print("В массиве", array, '\n', "Двум кратно ", len(crat_2), " чисел, \n Трем - ", len(crat_3))
print( " Четырем - ", len(crat_4), "\n Пяти - " , len(crat_5), "\n Шести - " , len(crat_6))
print( " Семи - ", len(crat_7),  "\n Восьми - " , len(crat_8),  "\n Девяти - " , len(crat_9))
