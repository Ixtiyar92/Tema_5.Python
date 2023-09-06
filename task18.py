# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


# n = int(input())  
# A = list(map(int, input().split())) 
# x = int(input())

# result = 0 
# count = 0
# for i in range(n):
#     if A[i] < x :
#         result = A[i]
#         count += 1
#     else:
#         print (f"i={i}")
#         result = A[i]
#         break
# print(result)

from random import randint
len_nums = int(input('Введите длину списка: '))
nums = [randint(1, 100) for i in range(len_nums)]
print("Список: ", *nums)
x = int(input('Введите число, которое нужно найти в списке: '))

# easy
min_diff = nums[0]
for i in nums:
    diff_current = abs(i-x)
    if diff_current < min_diff:
        res = i
        min_diff = diff_current

res = min([i for i in nums if abs(i-x) == min_diff])
print(f'Результат - {res}')

# pro
print(f'Результат - {min(nums, key=lambda y: abs(y-x))}')