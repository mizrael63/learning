#2.2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, 
#то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#вариант 0
def numer1(nat):
    nat = str(nat)
    chet = []
    nechet = []
    for i in nat:
        if int(i) % 2 == 0:
            chet.append(i)
        else: 
            nechet.append(i)
    chet = "".join(chet)
    nechet = "".join(nechet)
    a = len(chet)
    b = len(nechet)
    return a, b
#Результаты замеров 7,77 7,38 и 7,47 usec per loop для числа 12345678987654321
#по оценке степени сложности: 
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 <ipython-input-39-5593063bda24>:1(numer1)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      30    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       2    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#для одного числа функция выполняется за 1,21 usec, для двух 1,65 usec, для трех - 2,01 usec, для 4 - 2,49 usec
#по сути каждое добавляемое число увеличивает время выполнения примерно на 0,4 0,5 usec 
#если брать изначальную сложность за o, то удлиннение подаваемых на вход чисел добавляет примерно 0,5*n, где n - количество чисел
#сложность будет считаться как o+0,5*n / o+0,4*n
#для проверки возьмем за n число 20. По нашей формуле, при o = 1,3 usec итоговое время выполнения будет 1,3 + 10 ~ 11,3 usec (для 0,5)
#и 1,3 + 8 для 0,4 - ~ 9,3 usec
#При проверке получился результат в 8,44 8,65 и 8,5
    
# вариант 1
def numer2(num):
    even, odd = 0, 0 #четные even, нечетные odd
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd
#Результаты замеров 4,66 4,39 и 4,36 usec per loop для числа 12345678987654321
#по оценке степени сложности: 
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <ipython-input-38-83e811e0a2e4>:17(numer2)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#в сравнении с первым вариантом время выполнения O(1) составляет всего 0,420 usec или 420 nsec
#прирост за добавляемое число составляет примерно 185 nsec
#Значит при 20 цифрах в числе, время выполнения составит o + 185*20 nsec - 4,12 usec
#Фактические результаты - 5,35 5,36, 5,38

# вариант 2
def numer3(num):
    num = str(num)
    even = odd = 0
    for i in num:
        if i in {'0', '2', '4', '6', '8'}:
            even += 1
        else:
            odd += 1
    return even, odd

#Результаты замеров 1,91 1,76 и 1,87 usec per loop для числа 12345678987654321
#по оценке степени сложности: 
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <ipython-input-37-2874538b0968>:28(numer3)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#в сравнении с первым вариантом время выполнения O(1) составляет всего 0,580 usec или 580 nsec
#Средние величины, на основании 5 раз выполнения, при увеличении числа на 1
#640 (60)
#740 (100)
#820 (80)
#935 (115)
#1007 (72)
#1100 (93)
#1160 (60)
#Средний прирост время выполнения функции составляет 83 nsec. Для 20 элемнетов это будет o + 20 * 83 - 2240 nsec или 2,2 usec
#Результаты 2,14 2,31 2,17

#Общий вывод: функция 1 оптимизирована хуже всего, основные проблемы в том, что один и тот же метод вызывается столько же раз, сколько само число
#по длине. Вдобавок сама функция использует внутри себя больше переменных чем остальные. В результате даже обработка одной входной цифры
#отнимает в 3 раза больше времени чем во втором случае и в 2,5 - в третьем.
#Получая на вход одно и тоже число, в первом случае получается зависимость 8+N, где N - размер числа, а во втором и в третьем просто 4 вызываемых функции.
#При этом анализируя быстродействие - хранение предопределенной таблицы, с которой происходит сравнение позволяет пусть и затратив больше памяти в первичном
#вызове, сэкономить на последующей работе увеличивая таблицу. Вторая функция проигрывает третьей именно из-за этого. Поскольку третья затрачивает
#на каждое увеличение входного числа минимум памяти и обрабатывает функцию в разы быстрее
