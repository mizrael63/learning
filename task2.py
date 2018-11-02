#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, 
#то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
nat = str(input("Введите натуральное число"))
chet = []
nechet = []
for i in nat:
    if int(i) % 2 == 0:
        chet.append(i)
    else: nechet.append(i)
chet = "".join(chet)
nechet = "".join(nechet)
print("Количество четных цифр в вашем числе - ", len(chet), ", а нечетных - ", len(nechet))
