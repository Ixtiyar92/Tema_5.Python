# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

x = (int(input("Введите трёхзначное число: ")))
x1 = x%10
x2 = (x%100 - x1)//10
x3 = x//100 
print(x1+x2+x3)