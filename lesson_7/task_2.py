#функция в итоге так и не работает даже в таком виде. Судя по всему он где-то стал подставлять temp, вместо нормальных
#значений, но даже когда этого не делал, всё равно у меня не получилось для него сделать нормальную рекурсию

# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
# Из того что я понял, метод слияния состоит в разбиении одного массива на два примерно одинаковых
# внутри каждого получившегося массива производится своя сортировка, причем она может выполняться тем же способом
# после чего уже отсортированные элементы соединяются в одну общую последовательность и собираются обратно
# представим логически
# на вход некая функция получает массив.
# Для каждого получившегося массива будет вызываться функция сортировки и разбиения
#
#
#
import random

# задаем максимальное количество элементов
SIZE = 16
array = [random.randint(0, 50) for _ in range(SIZE)]
print("Исходный массив :", array)
zeta = array


def delitel(array):
    global zeta

    def sort(a):
        i = 0
        while i <= len(a):
            for n in range(len(a) - 1 - i):
                if a[n] > a[n + 1]:
                    a[n], a[n + 1] = a[n + 1], a[n]
            i += 1

    d = int(len(array)/2)
    ar = array[0:d]
    sort(ar)

    ray = array[d:len(array)]
    sort(ray)

    # создаем список куда будем записывать
    temp = [array for array in range(SIZE)]

    def summator(ar, ray):
        i = 0
        i2 = 0
        while i < len(ar) and i < len(ray):
            if ar[i] < ray[i]:
                temp[i2] = ar[i]
                temp[i2 + 1] = ray[i]
                i += 1
                i2 += 2
            else:
                temp[i2] = ray[i]
                temp[i2 + 1] = ar[i]
                i += 1
                i2 += 2
            break


    summator(ar, ray)

    zeta = summator(ar, ray)
    return zeta


delitel(array)


def callabled(zeta):
    j = 0
    while j < 40:
        #    while (all(zeta[ss]<zeta[ss+1] for ss in range(len(zeta)-1))) != True:
        zeta = delitel(zeta)
        j += 1


callabled(zeta)

print(zeta)