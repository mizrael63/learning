#6. Написать программу, где генерируется случайное целое число от 0 до 100
#Пользователь должен его отгадать максимум за 10 попыток.
#После каждой неудачи должно сообщаться, больше или меньше загаданного то число, что ввел пользователь.
#Если за 10 попыток число не отгадано – вывести его. 
 
import numpy as np
import random
 
a = 0
n = 0
i = 0
def start():
    generator()
def generator():
    global a
    global n
    a = int(np.random.random_integers(0, 100, 1))
    n = 10
    ugadaika()
def check_n():
    if n == 0:
        print("К сожалению вы исчерпали число попыток")
        print("Мы загадывали вам число ", a)
        d = input("Если хотите начать новую игру, введите 1")
        if d == "1":
            generator()
        else: 
            exit
    else:
        ugadaika()
def ugadaika():
    global i
    global n
    i = int(input("Введите угадываемое число: "))
    if i == a:
        print("Вы угадали число")
    elif i > a:
        print("Вы ввели число больше загаданного")
        n = n - 1
        print("У вас осталось ", n, "попыток")
        check_n()
    elif i < a:
        n = n - 1
        print("Вы ввели число меньшее, чем загаданное")
        print("У вас осталось ", n, "попыток")
        check_n()

start()