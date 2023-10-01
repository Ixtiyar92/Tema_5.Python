# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)

start_d, end_d = (int(input("Начало диапазона: ")), int(input("Конец диапазона: "))) # получаем на вход начало и конец диапазона
num_list = list(map(int, input().split())) # получаем на вход список чисел

# Способ 1: через генератор списков
result = [i for i in range(len(num_list)) if (num_list[i] <= end_d and num_list[i] >= start_d)]
# в список попадают индексы элементов, для которых выполняется условие задачи
print(result)

# Способ 1: через циклы
res_1 = []
for i in range(len(num_list)):
    if (num_list[i] <= end_d and num_list[i] >= start_d):
        res_1.append(i)
print(res_1)