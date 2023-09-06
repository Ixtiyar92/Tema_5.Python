# Задача 19: Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Ввод: 1 2 3 4 5 6 -> 4 5 6 1 2 3 (сдвиг на 3 элемента вправо)

lst = list(map(int, input("Введите список чисел через пробел: ").split()))
k = int(input("Введите число K: ")) % len(lst)
print(lst[k:] + lst[:k])