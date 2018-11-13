from collections import defaultdict
i = 0
a = int(input("Введите количество предприятий: "))
dictionary = defaultdict()
print("Вводимые наименования и данные разделяются с помощью enter")
while i < a:
    name, quart1, quart2, quart3, quart4  = (input("Введите название предприятия и его прибыль за 4 квартала: ") for _ in range(5))
    quart1, quart2, quart3, quart4 = int(quart1), int(quart2), int(quart3), int(quart4)
    print("Осталось ввести данные по ", a - i - 1, "предприятиям")
    dictionary[name] = [quart1 + quart2 + quart3 + quart4]
    i += 1
print('\n')
keys = list(dictionary.keys())
values = list(dictionary.values())

i = 0
for_sum = []
while i < len(values):
    for_sum = for_sum + values[i]
    i += 1
average = sum(for_sum) / len(values)

i = 0
while i < len(values):
    if for_sum[i] > average:
        print("Фирма", keys[i], "сделала выручки больше среднего")
    i += 1
print("\nСредняя годовая прибыль составила", average,'\n')
i = 0
while i < len(values):
    if for_sum[i] < average:
        print("Фирма", keys[i], "сделала выручки меньше среднего")
    i += 1