#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
#Из того что я понял, метод слияния состоит в разбиении одного массива на два примерно одинаковых
#внутри каждого получившегося массива производится своя сортировка, причем она может выполняться тем же способом
#после чего уже отсортированные элементы соединяются в одну общую последовательность и собираются обратно
#представим логически
#на вход некая функция получает массив. Необходимо проанализировать его длину, если четная, то разбить пополам,
#если нет, то на n и n+1 элементов соответственно.
#Для каждого получившегося массива будет вызываться функция сортировки и разбиения
#
#
#
import random
array = [random.randint(0, 50) for _ in range(16)]
print("Исходный массив :",array)

def delitel(array):
    d = int(len(array) / 2)
    ar = array[0:d]

    while all(ar[dd] < ar[dd + 1] for dd in range(len(ar) - 1)) == False:
        dd = 0
        while dd <= len(ar):
            for dd in range(len(ar) - 1 - dd):
                if ar[dd] > ar[dd + 1]:
                    ar[dd], ar[dd + 1] = ar[dd + 1], ar[dd]

            dd +=1
            break

    ray = array[d:len(array)]
    while all(ray[bb] < ray[bb + 1] for bb in range(len(ray) - 1)) == False:
        bb = 0
        while bb <= len(ray):
            for bb in range(len(ray) - 1 - bb):
                if ray[bb] > ray[bb + 1]:
                    ray[bb], ray[bb + 1] = ray[bb + 1], ray[bb]

            bb += 1
            break
    temp = [i for i in range(16)]
    print("Результат прохождения итераций", ar, ray, temp)

    def summator(ar, ray):
        i = 0
        i2 = 0
        while i < len(ar) and i < len(ray):
            if ar[i] < ray[i]:
                temp[i2] = ar[i]
                temp[i2+1] = ray[i]
                i += 1
                i2 += 2

            else:
                temp[i2] = ray[i]
                temp[i2+1] = ar[i]
                i += 1
                i2 += 2

        return temp
    summator(ar, ray)
    global zeta
    print(temp)
    zeta = temp
    return zeta
    #если длина ар или рей больше 1 элемента, опять вызывать эту же функцию
    #вызываем функцию пока хз как, которая на вход будет получать элементы ар и рей и суммировать их в накопительный
    #элемент z

#d = int(len(array)/2)
#ar = array[0:d]
#ray = array[d:len(array)]
#print(ar, ray)
#z = []
#if len(ar)==len(ray):
#    i = 0
#    while i < len(ray):
#        if ar[i]<ray[i]:
#            z = z + [ar[i], ray[i]]
#        else:
#            z = z + [ray[i], ar[i]]
#        i += 1
# print(z)

delitel(array)
print(max(array), min(array))
def callabled():
    while (all(zeta[ss]<zeta[ss+1] for ss in range(len(zeta)-1))) != True:
        zeta = delitel(zeta)
        break
print(zeta)


print(callabled(), zeta)
