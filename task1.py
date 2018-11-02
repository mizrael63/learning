
#Написать программу, которая будет складывать, вычитать, умнождать или делить два числа. 
#Числа и знак операции вводятся пользователем
first = 0
second = 0
operand = 0
def start():
    global operand
    global first   
    global second
    operand = input("Введите знак операции")
    first = int(input("Введите первое число "))
    second = int(input("Введите второе число"))
    proverka(operand)
def summm(first, second):
    result = first + second
    return result
def unmog(first, second):
    result = first * second
    return result
def raznost(first, second):
    result = first - second
    return result
def delenie(first, second):
    if second == 0:
        print("Деление на ноль запрещено")
        start()
    else:
        result = first / second
    return result
def proverka(operand):
    if operand == "0":
        print("Работа приложения прервана пользователем. Для возобновления введите 1")
        a = input("Ожидается ввод")
        if a == "1":
            start()
        else: exit
    elif operand =="+":
        print("Результат суммы: ",summm(first,second))
        start()
    elif operand == "-":
        print("Результат разности: ",raznost(first, second))
        start()
    elif operand == "*":
        print("Результат умножения: ",unmog(first, second))
        start()
    elif operand == "/":
        print("Результат деления: ",delenie(first, second))
        start()
    else:
        operand = input("Некорректное действие, введите знак действия заново ")
        proverka(operand)

start()
