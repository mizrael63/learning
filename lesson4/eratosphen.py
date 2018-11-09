def eratosthenes(n):     # n - число, до которого хотим найти простые числа 
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

def call(i):
	n = i * 10
	a = list(filter(lambda x: x != 0, eratosthenes(n)))
	return a[i]
#При вызове call(50) получены результаты 917, 915 и 921 usec, потому что n задавался как i * i. При уменьшении n до i*5 результаты
#составили 84,8 82,2 и 87,3 usec для 100 loops
#это тесты для решета Эратосфена
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <ipython-input-35-9eb47342639f>:11(call)
#      251    0.000    0.000    0.000    0.000 <ipython-input-35-9eb47342639f>:13(<lambda>)
#        1    0.000    0.000    0.000    0.000 <ipython-input-35-9eb47342639f>:2(eratosthenes)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       53    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# При поиске 500ого числа:
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <ipython-input-36-6c55043eaed1>:11(call)
#     2501    0.000    0.000    0.000    0.000 <ipython-input-36-6c55043eaed1>:13(<lambda>)
#        1    0.001    0.001    0.001    0.001 <ipython-input-36-6c55043eaed1>:2(eratosthenes)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      367    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

inumerate = 1
num = 2 
aaaa = []
def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def ravno(num):
    global inumerate
    global aaaa
    if IsPrime(num) == 1:
        aaaa.append(num)
        inumerate += 1
def work(i):
    global num
    global aaaa
    while inumerate < i:
        ravno(num)
        num += 1
    return aaaa
def called(i):
    work(i+2)
    return aaaa[i]

#Результат получился интересный. Командная строка выдала the test results are likely unrealiable. 
#The worst time was more than four times slower then the best time
#Результаты при этом для каждого прогона (худший - лучший)
#2,59 usec - 383 nsec
#2,73 usec - 377 nsec
#2,6 usec - 380 nsec
#Разброс конечно приличный, потому и предупреждение, зато результаты достигаются в среднем в 16 раз быстрее.
#Тест функции выглядит следующим образом (для тех же 50 повторений)
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      232    0.000    0.000    0.000    0.000 <ipython-input-112-35bea38014fc>:12(ravno)
#        1    0.000    0.000    0.000    0.000 <ipython-input-112-35bea38014fc>:18(work)
#        1    0.000    0.000    0.000    0.000 <ipython-input-112-35bea38014fc>:25(called)
#      232    0.000    0.000    0.000    0.000 <ipython-input-112-35bea38014fc>:5(IsPrime)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       51    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# аналогично решету - при поиске 500 числа:
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     3580    0.001    0.000    0.005    0.000 <ipython-input-113-4bc6f194577b>:12(ravno)
#        1    0.001    0.001    0.006    0.006 <ipython-input-113-4bc6f194577b>:18(work)
#        1    0.000    0.000    0.006    0.006 <ipython-input-113-4bc6f194577b>:25(called)
#     3580    0.004    0.000    0.004    0.000 <ipython-input-113-4bc6f194577b>:5(IsPrime)
#        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#      501    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#В итоге если смотреть на cProfile, то второй вариант однозначно хуже. Но после прогона на скорость ещё раз в командной строке только уже для 500
#элементов, в первом случае я был вынужден увеличить значение n до i*10, потому что в противном случае вызываемый элемент в массиве отсутствовал
#Время выполнения функции составило 1,82 1,83 1,84 msec per loop, в то время как у самописной функции стало
#61,6 usec - 410 nsec
#65,5 usec - 423 nsec
#62,5 usec - 443 nsec

