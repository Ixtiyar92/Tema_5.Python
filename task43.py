# Задача 43: Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на одной строке через пробел.
# 1 2 1 3 4 5 3 4 -> 3
# 1 2 1 3 4 3 1 -> 2

# Способ 1: через множество
list = [1, 2, 1, 3, 4, 5, 3, 4, 1]
pair_count = sum(list.count(i)//2 for i in set(list))
# pair_count - количество пар
print(pair_count)


# Способ 2: 
# def count_ps():
#     arr = input("input: ").split()
#     arr = list(map(int, arr))
#     count = 0
#     while len(arr) > 1:
#         x = arr.pop()
#         # print(arr)
#         if x in arr:
#             count +=1
#             arr.remove(x)
#             print(arr)
#     return count
# print(count_ps())