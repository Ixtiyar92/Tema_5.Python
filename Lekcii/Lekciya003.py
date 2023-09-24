# def sum_numbers(n): # создаём функцию sum_numbers, которая считает сумму всех элементов от 1 до n
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     print(summa)
# sum_numbers(5)

# или:
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
# a = sum_numbers(5)
# print(a)

# def sum_str(*args): # функция, принимающая неограниченное кол-во аргументов
#     res = "" # тип данных строка
#     for i in args:
#         res += i
#     return res
# print(sum_str("q", "e", "l"))



# import modul1
# print(modul1.max1(5, 9))

# или:
# from modul1 import max1
# print(max1(10, 9))

# или:
# from modul1 import * # импорт всех функций из файла modul1
# print(max1(10, 9))

# или:
# import modul1 as m1 # Alias (псевдоним) — альтернативное имя, которое даётся функции при еt импорте из файла
# print(m1.max1(10, 9))



# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

def quick_sort(array): # быстрая сортировка
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return  quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14, 5, 9, 7, 8, 6, 3, 10, 89]))

def merge_sort(nums): # сортировка слиянием
    if len(nums) > 1:
        mid = len(nums) // 2 # делим список надвое, пока не остается один элемент
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list1 = [1,5,6,8,3,0,98,67,546,34,87,10]
merge_sort(list1)
print(list1)