# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1
# 2
# 5
# Output:
# 1, 3, 5, 7, 9

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количесто элементов: "))
# решение циклом
for i in range(n):
    print(a1 + i * d)

# решение через генератор:
progression = [a1 + (i-1) * d for i in range(1, n+1)]
print(progression)