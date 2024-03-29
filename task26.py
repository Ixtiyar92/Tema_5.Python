# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# Пример:
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))

# def Pow (number: int, rank: int):
#     "Возведение в степень (rank) числа (number)"
#     if (rank==0): 
#         return 1
#     result = number * Pow (number, rank-1)
#     return result

# print (Pow (A,B))

# или:
def power (a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))
result = power(A, B)
print(f"{A} в степени {B} равно {result}")