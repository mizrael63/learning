#Задача 5.В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
SIZE = 50
SIZE_O = -50
array = [random.randint(SIZE_O, SIZE) for _ in range(SIZE)]
reg_1 = SIZE_O #Записываем число. Изначально берем минимальное значение массива
reg_2 = 0 #Записываем позицию
count = 0
for i in array:
    if (i < 0 and i > reg_1):
        reg_1 = i
        reg_2 = count
  
    count +=1

print("Массив: ", array)    
print("Максимальный отрицательный элемент: ", reg_1)
print("Позиция в массиве: ", reg_2)
