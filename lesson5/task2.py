def iter_1(d): #тут мы превращаем наше шестнадцитиричное число в десятичное
    d = deque(d, maxlen=len(d))
    d.reverse()
    b = deque([], maxlen=len(d))
    i = 0
    while i < len(d):
        b.append(x[d[i]])
        i += 1
    i = 0
    g = deque([])
    while i < len(b):
        g.append(int(b[i])*16**i)
        i += 1
    b = sum(g)
    return b
def iter_2(d): #здесь получаем обратный результат
    q = deque([])
    while d > 0:
        b = d % 16
        q.append(b)
        d = int((d - b) / 16)
    q = deque(q, maxlen=len(q))
    return q
def iter_3(d): #а тут преобразуем десятичную запись к шестнадцатиричному виду
    i = 0
    a = str()
    while i < len(d):
        a += x_rev[d[i]]
        i += 1
    return a

from collections import deque

#блок создания прямого и обратного словаря
keyz = '0', "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"
valuez = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
x = dict(zip(keyz, valuez))
x_rev = dict(zip(valuez, keyz))

# запрос данных пользователя
first = list(input("Введите первое число. Буквы вводятся в большом регистре: "))
second = list(input("Введите второе число. Буквы вводятся в большом регистре: "))

# нахождение суммы и произведения чисел
summ = iter_1(first)+ iter_1(second)
proizv = iter_1(first) * iter_1(second)

# разворот чисел.. в функции не отрабатывал корректно пришлось вынести
z_sum = iter_2(summ)
z_sum.reverse()
z_proizv = iter_2(proizv)
z_proizv.reverse()

#Правильная запись итоговых значений
print("Сумма чисел ", first, "и ", second, 'равняется ', iter_3(z_sum))
print(f"Произведение чисел ", first, "и ", second, 'равняется ', iter_3(z_proizv))
