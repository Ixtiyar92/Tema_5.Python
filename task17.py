# Задача 17: Дан список чисел.
# Определите, сколько в нём встречается различных чисел.

# сделать список из неповторяющихся элементов:
nums = [1, 2, 3, 4, 1, 2]
# print(len(set(nums)))

# элементы, встречающиеся 1 раз
uniq_nums = [i for i in nums if nums.count(i) == 1]
uniq_nums1 = []

for i in nums:
    if nums.count(i) == 1:
        uniq_nums1.append(i)

print(uniq_nums)
print(uniq_nums1)